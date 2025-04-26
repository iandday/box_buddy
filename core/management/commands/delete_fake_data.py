import logging

from django.core.management.base import BaseCommand

from core.models import URL
from core.models import Box
from core.models import File
from core.models import Item
from core.models import Location

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Removes fake data from all models created using the generate_fake_data command"

    def handle(self, *args, **kwargs):
        for obj in [Location, Box, Item, File, URL]:
            obj.objects.filter(description__endswith=":FAKE").delete()

        logger.info("Generated data deleted successfully")
