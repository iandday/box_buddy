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

if [[ ${DEV} == "True" ]]; then
    exec watchfiles --filter python celery.__main__.main --args '-A box_buddy.celery worker -l INFO'
else
    exec celery -A celery worker -l INFO

fi

