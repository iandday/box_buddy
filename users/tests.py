import pytest

from users.models import User


@pytest.mark.django_db
def test_create_superuser():
    email = "admin@example.com"
    password = "securepassword123"  # noqa: S105

    # Create a superuser using the custom manager
    superuser = User.objects.create_superuser(email=email, password=password)

    # Assertions to verify the superuser was created correctly
    assert superuser.email == email
    assert superuser.is_admin is True
    assert superuser.is_staff is True
    assert superuser.check_password(password) is True


@pytest.mark.django_db
def test_create_user():
    email = "user@example.com"
    password = "userpassword123"  # noqa: S105

    # Create a regular user using the custom manager
    user = User.objects.create_user(email=email, password=password)

    # Assertions to verify the user was created correctly
    assert user.email == email
    assert user.is_admin is False
    assert user.is_staff is False
    assert user.check_password(password) is True


@pytest.mark.django_db
def test_create_user_without_email():
    password = "password123"  # noqa: S105

    # Attempt to create a user without an email and expect a ValueError
    with pytest.raises(ValueError, match="Users must have an email address"):
        User.objects.create_user(email=None, password=password)


@pytest.mark.django_db
def test_user_str_representation():
    email = "testuser@example.com"
    password = "password123"  # noqa: S105

    # Create a user and verify the string representation
    user = User.objects.create_user(email=email, password=password)
    assert str(user) == email
