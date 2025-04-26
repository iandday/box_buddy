import logging
import os
import random

from django.core.management.base import BaseCommand
from faker import Faker

from core.models import URL
from core.models import Box
from core.models import File
from core.models import Item
from core.models import Location
from users.models import User

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Generate fake data for all models and link them together"

    def handle(self, *args, **kwargs):
        fake = Faker()

        user = User.objects.get(email=os.environ["DJANGO_SUPERUSER_EMAIL"])

        # Create Locations
        locations = []
        for name in ["House", "Shed", "Garage", "Basement"]:
            location, _ = Location.objects.get_or_create(
                name=name,
                defaults={"description": f"{fake.text()}:FAKE"},
                created_by=user,
            )
            locations.append(location)
            logger.debug("Created location: %s", location)

        # Create Boxes
        boxes = []
        for _ in range(10):
            box = Box.objects.create(
                name=fake.word(),
                description=f"{fake.text()}:FAKE",
                created_by=user,
                location=random.choice(locations),  # noqa: S311
            )
            boxes.append(box)
            logger.debug("Created box: %s", box)

        # Create Items
        items = []
        for _ in range(20):
            item = Item.objects.create(
                name=fake.word(),
                description=f"{fake.text()}:FAKE",
                quantity=random.randint(1, 100),  # noqa: S311
                created_by=user,
                box=random.choice(boxes),  # noqa: S311
            )
            items.append(item)
            logger.debug("Created item: %s", item)

        # Create Files
        for _ in range(10):
            f = File.objects.create(
                name=fake.file_name(),
                description=f"{fake.text()}:FAKE",
                file=fake.file_path(),
                created_by=user,
                item=random.choice(items),  # noqa: S311
                box=random.choice(boxes),  # noqa: S311
                location=random.choice(locations),  # noqa: S311
            )
            logger.debug("Created file: %s", f)

        # Create URLs
        for _ in range(10):
            u = URL.objects.create(
                name=fake.word(),
                description=f"{fake.text()}:FAKE",
                url=fake.url(),
                created_by=user,
                item=random.choice(items),  # noqa: S311
                box=random.choice(boxes),  # noqa: S311
                location=random.choice(locations),  # noqa: S311
            )
            logger.debug("Created URL: %s", u)
        logger.info("Fake data generated successfully")
