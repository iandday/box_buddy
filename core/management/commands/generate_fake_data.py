import logging
import os
import random

from django.core.management.base import BaseCommand
from faker import Faker

from core.models import URL
from core.models import Box
from core.models import File
from core.models import Item
from users.models import User

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Generate fake data for all models and link them together"

    def handle(self, *args, **kwargs):
        fake = Faker()

        user = User.objects.get(email=os.environ["DJANGO_SUPERUSER_EMAIL"])

        # Create Parent Boxes
        for name in ["House", "Shed", "Garage", "Basement"]:
            box = Box.objects.get_or_create(
                name=name,
                fake=True,
                defaults={
                    "description": f"{fake.text()}",
                    "created_by": user,
                },
            )
            logger.debug("Created parent box: %s", box)

        # Create Boxes
        boxes = []
        parent_boxes = Box.objects.filter(parent__isnull=True)
        for _ in range(10):
            box = Box.objects.create(
                name=fake.word(),
                description=f"{fake.text()}",
                parent=parent_boxes[random.randint(0, len(parent_boxes) - 1)],  # noqa: S311
                slug=fake.slug(),
                is_active=True,
                is_deleted=False,
                fake=True,
                created_by=user,
            )
            boxes.append(box)
            logger.debug("Created box: %s", box)

        # Create Items
        items = []
        for _ in range(20):
            item = Item.objects.create(
                name=fake.word(),
                description=f"{fake.text()}",
                quantity=random.randint(1, 100),  # noqa: S311
                created_by=user,
                fake=True,
                box=random.choice(boxes),  # noqa: S311
            )
            items.append(item)
            logger.debug("Created item: %s", item)

        # Create Files
        for _ in range(10):
            f = File.objects.create(
                name=fake.file_name(),
                description=f"{fake.text()}",
                file=fake.file_path(),
                created_by=user,
                fake=True,
                item=random.choice(items),  # noqa: S311
                box=random.choice(boxes),  # noqa: S311
            )
            logger.debug("Created file: %s", f)

        # Create URLs
        for _ in range(10):
            u = URL.objects.create(
                name=fake.word(),
                description=f"{fake.text()}",
                url=fake.url(),
                created_by=user,
                fake=True,
                item=random.choice(items),  # noqa: S311
                box=random.choice(boxes),  # noqa: S311
            )
            logger.debug("Created URL: %s", u)
        logger.info("Fake data generated successfully")
