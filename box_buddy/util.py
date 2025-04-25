import random
import string

from django.utils.text import slugify


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return "".join(random.choice(chars) for _ in range(size))  # noqa: S311


def unique_slug_generator(instance, new_slug=None):
    slug = new_slug if new_slug is not None else slugify(instance.name)
    klass = instance.__class__
    max_length = klass._meta.get_field("slug").max_length  # noqa: SLF001
    slug = slug[:max_length]
    qs_exists = klass.objects.filter(slug=slug).exists()

    if qs_exists:
        new_slug = f"{slug[: max_length - 5]}-{random_string_generator(size=4)}"

        return unique_slug_generator(instance, new_slug=new_slug)
    return slug
