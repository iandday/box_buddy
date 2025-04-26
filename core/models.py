import uuid

from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from box_buddy.util import unique_slug_generator
from users.models import User


class Location(models.Model):
    """
    Location Model

    Represents a physical or logical location with attributes for identification,
    metadata, and status.

    Attributes:
        id (UUIDField): The primary key for the location, automatically generated as a UUID.
        slug (SlugField): A unique, optional slug for the location, used for URL-friendly identifiers.
        created_by (ForeignKey): The user who created the location, linked to the User model.
        created_at (DateTimeField): The timestamp when the location was created, automatically set.
        updated_by (ForeignKey): The user who last updated the location, linked to the User model. Optional.
        updated_at (DateTimeField): The timestamp when the location was last updated, automatically set.
        name (CharField): The unique name of the location.
        description (TextField): An optional description of the location.
        is_active (BooleanField): Indicates whether the location is active. Defaults to True.
        is_deleted (BooleanField): Indicates whether the location is marked as deleted. Defaults to False.

    Methods:
        __str__(): Returns the string representation of the location, which is its name.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = models.SlugField(max_length=250, null=True, blank=True, unique=True)
    created_by = models.ForeignKey(User, related_name="created_by_location", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(
        User, related_name="updated_by_location", on_delete=models.CASCADE, null=True, blank=True
    )
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Box(models.Model):
    """
    Box Model

    Represents a storage box with hierarchical relationships, location, and metadata.

    Attributes:
        id (UUIDField): Unique identifier for the box, automatically generated.
        slug (SlugField): Optional unique slug for the box, used for URL-friendly identifiers.
        created_by (ForeignKey): Reference to the user who created the box.
        created_at (DateTimeField): Timestamp of when the box was created.
        updated_by (ForeignKey): Reference to the user who last updated the box (optional).
        updated_at (DateTimeField): Timestamp of the last update to the box.
        parent (ForeignKey): Optional reference to a parent box, enabling hierarchical relationships.
        name (CharField): Name of the box, required and unique within a location.
        description (TextField): Optional description of the box.
        location (ForeignKey): Reference to the location where the box is stored.
        is_active (BooleanField): Indicates whether the box is active (default is True).
        is_deleted (BooleanField): Indicates whether the box is marked as deleted (default is False).

    Meta:
        verbose_name_plural: Plural name for the model in the admin interface.
        constraints: Ensures that the combination of `name` and `location` is unique.

    Methods:
        __str__(): Returns the name of the box as its string representation.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = models.SlugField(max_length=250, null=True, blank=True, unique=True)
    created_by = models.ForeignKey(User, related_name="created_by_box", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(User, related_name="updated_by_box", on_delete=models.CASCADE, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE, related_name="children")
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="location")
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Boxes"
        constraints = [models.UniqueConstraint(fields=["name", "location"], name="unique box")]

    def __str__(self):
        return self.name


class Item(models.Model):
    """
    Item Model

    Represents an item that can be stored in a box. Each item has a unique identifier,
    a name, and optional descriptive fields. Items are associated with a box and
    can be created or updated by a user.

    Attributes:
        id (UUIDField): The unique identifier for the item.
        slug (SlugField): A unique slug for the item, optional.
        created_by (ForeignKey): The user who created the item.
        created_at (DateTimeField): The timestamp when the item was created.
        updated_by (ForeignKey): The user who last updated the item, optional.
        updated_at (DateTimeField): The timestamp when the item was last updated.
        name (CharField): The name of the item.
        description (TextField): A description of the item, optional.
        quantity (IntegerField): The quantity of the item, defaults to 1.
        box (ForeignKey): The box the item belongs to, optional.
        is_active (BooleanField): Indicates if the item is active, defaults to True.
        is_deleted (BooleanField): Indicates if the item is deleted, defaults to False.

    Meta:
        constraints: Ensures that the combination of `name` and `box` is unique.

    Methods:
        __str__(): Returns the string representation of the item, which is its name.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = models.SlugField(max_length=250, null=True, blank=True, unique=True)
    created_by = models.ForeignKey(User, related_name="created_by_item", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(
        User, related_name="updated_by_item", on_delete=models.CASCADE, null=True, blank=True
    )
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    quantity = models.IntegerField(default=1)
    box = models.ForeignKey(Box, on_delete=models.CASCADE, related_name="box", null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        constraints = [models.UniqueConstraint(fields=["name", "box"], name="unique item")]

    def __str__(self):
        return self.name


class File(models.Model):
    """
    Represents a file entity in the system, which can be associated with an item, box, or location.

    Attributes:
        id (UUIDField): The unique identifier for the file.
        slug (SlugField): A unique slug for the file, optional.
        created_by (ForeignKey): The user who created the file.
        created_at (DateTimeField): The timestamp when the file was created.
        updated_by (ForeignKey): The user who last updated the file, optional.
        updated_at (DateTimeField): The timestamp when the file was last updated.
        name (CharField): The name of the file.
        description (TextField): A description of the file, optional.
        file (FileField): The file itself, stored in the "files/" directory.
        item (ForeignKey): The item associated with the file.
        box (ForeignKey): The box associated with the file, optional.
        location (ForeignKey): The location associated with the file, optional.
        is_active (BooleanField): Indicates whether the file is active.
        is_deleted (BooleanField): Indicates whether the file is deleted.

    Meta:
        constraints (list): Ensures that the combination of name, item, box, and location is unique.

    Methods:
        __str__(): Returns the name of the file as its string representation.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = models.SlugField(max_length=250, null=True, blank=True, unique=True)
    created_by = models.ForeignKey(User, related_name="created_by_file", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(
        User, related_name="updated_by_file", on_delete=models.CASCADE, null=True, blank=True
    )
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to="files/")
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="location_file")
    box = models.ForeignKey(Box, on_delete=models.CASCADE, related_name="box_file", null=True, blank=True)
    location = models.ForeignKey(
        Location, on_delete=models.CASCADE, related_name="location_file", null=True, blank=True
    )
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        constraints = [models.UniqueConstraint(fields=["name", "item", "box", "location"], name="unique file")]

    def __str__(self):
        return self.name


class URL(models.Model):
    """
    Represents a URL that stores information about URLs associated with items, boxes, or locations.

    Attributes:
        id (UUIDField): The primary key for the URL, generated automatically as a UUID.
        slug (SlugField): An optional slug field for the URL, unique and limited to 250 characters.
        created_by (ForeignKey): A reference to the user who created the URL.
        created_at (DateTimeField): The timestamp when the URL was created, set automatically.
        updated_by (ForeignKey): A reference to the user who last updated the URL, optional.
        updated_at (DateTimeField): The timestamp when the URL was last updated, set automatically.
        description (TextField): An optional text field for additional information about the URL.
        name (CharField): The name of the URL, limited to 255 characters.
        url (URLField): The actual URL being stored.
        item (ForeignKey): An optional reference to an associated item.
        box (ForeignKey): An optional reference to an associated box.
        location (ForeignKey): An optional reference to an associated location.
        is_active (BooleanField): Indicates whether the URL is active. Defaults to True.
        is_deleted (BooleanField): Indicates whether the URL is marked as deleted. Defaults to False.

    Meta:
        constraints: Ensures that the combination of name, item, box, and location is unique.

    Methods:
        __str__: Returns the string representation of the URL.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = models.SlugField(max_length=250, null=True, blank=True, unique=True)
    created_by = models.ForeignKey(User, related_name="created_by_url", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(User, related_name="updated_by_url", on_delete=models.CASCADE, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True)
    name = models.CharField(max_length=255)
    url = models.URLField()
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="item_url", null=True, blank=True)
    box = models.ForeignKey(Box, on_delete=models.CASCADE, related_name="box_url", null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="location_url", null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        constraints = [models.UniqueConstraint(fields=["name", "item", "box", "location"], name="unique url")]

    def __str__(self):
        return self.url


@receiver(pre_save, sender=Location)
def pre_save_receiver_location(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


@receiver(pre_save, sender=Box)
def pre_save_receiver_box(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


@receiver(pre_save, sender=Item)
def pre_save_receiver_item(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


@receiver(pre_save, sender=File)
def pre_save_receiver_file(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


@receiver(pre_save, sender=URL)
def pre_save_receiver_url(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
