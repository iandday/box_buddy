# type ignore[misc, no-untyped-def]
import os

from celery import Celery  # type: ignore[import-untyped]
from celery.signals import setup_logging  # type: ignore[import-untyped]

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "box_buddy.settings")
app = Celery("box_buddy")
app.config_from_object("django.conf:settings", namespace="CELERY")


@setup_logging.connect  # type ignore[misc]
def config_loggers(*args: object, **kwargs: object):
    from logging.config import dictConfig

    from django.conf import settings

    dictConfig(settings.LOGGING)


app.autodiscover_tasks()
