set -o errexit
set -o pipefail
set -o nounset

postgres_ready() {
python << END
import sys
import os
import psycopg2

try:
    psycopg2.connect(
        dbname=os.getenv('POSTGRES_DB'),
        user=os.getenv('POSTGRES_USER'),
        password=os.getenv('POSTGRES_PASSWORD'),
        host=os.getenv('POSTGRES_SERVER'),
        port=os.getenv('POSTGRES_PORT'),
    )
except psycopg2.OperationalError:
    sys.exit(-1)
sys.exit(0)
END
}
until postgres_ready; do
>&2 echo 'Waiting for PostgreSQL to become available...'
sleep 1
done
>&2 echo 'PostgreSQL is available'

python /app/src/manage.py migrate
python /app/src/manage.py createsuperuser --no-input || true
mkdocs build -f /app/src/mkdocs.yml
python /app/src/manage.py collectstatic --noinput

if [[ ${DEV} == "True" ]]; then
    exec python /app/src/manage.py runserver_plus 0.0.0.0:8000
else
    exec python -c /app/src/gunicorn_conf.py box_buddy.wsgi

fi
