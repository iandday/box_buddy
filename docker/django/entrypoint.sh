set -o errexit
set -o pipefail
set -o nounset

postgres_ready() {
uv run - << END
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
sleep 5
done
>&2 echo 'PostgreSQL is available'


if [[ ${CONTAINER_ROLE} == "beats" ]]; then
    rm -f './celerybeat.pid'
    uv run celery -A box_buddy.celery_app beat -l INFO
elif [[ ${CONTAINER_ROLE} == "worker" ]]; then
    uv run celery -A box_buddy.celery_app worker -l INFO
elif [[ ${CONTAINER_ROLE} == "flower" ]]; then
    uv run  celery \
            -A box_buddy.celery_app \
            -b "${CELERY_REDIS}" \
            flower \
            --basic_auth="${CELERY_FLOWER_USER}:${CELERY_FLOWER_PASSWORD}"
elif [[ ${CONTAINER_ROLE} == "server" ]]; then
    if [[ ${DEV} == "True" ]]; then
        uv run gunicorn --bind 0.0.0.0:8000 box_buddy.wsgi:application --reload
    else
        uv run gunicorn --bind 0.0.0.0:8000 box_buddy.wsgi:application
    fi
else
    echo "Unknown CONTAINER_ROLE: ${CONTAINER_ROLE}"
    exit 1
fi
