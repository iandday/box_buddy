import http

import pytest
from django.contrib.auth.models import User
from django.urls import reverse

from core.models import Location


@pytest.fixture
def create_user(db):
    return User.objects.create_user(username="testuser", password="password")  # noqa: S106


@pytest.fixture
def authenticated_client(client, create_user):
    client.login(username="testuser", password="password")  # noqa: S106
    return client


@pytest.fixture
def create_location(db):
    return Location.objects.create(name="Test Location", slug="test-location")


def test_home_view(client):
    response = client.get(reverse("home"))
    assert response.status_code == http.HTTPStatus.OK
    assert "pages/home.html" in [t.name for t in response.templates]


def test_about_view(client):
    response = client.get(reverse("about"))
    assert response.status_code == http.HTTPStatus.OK
    assert "pages/about.html" in [t.name for t in response.templates]


def test_location_list_view_unauthenticated(client):
    response = client.get(reverse("location_list"))
    assert response.status_code == http.client.FOUND  # Redirect to login


def test_location_list_view_authenticated(authenticated_client):
    response = authenticated_client.get(reverse("location_list"))
    assert response.status_code == http.HTTPStatus.OK
    assert "pages/location_list.html" in [t.name for t in response.templates]


def test_location_detail_view_unauthenticated(client, create_location):
    response = client.get(reverse("location_detail", kwargs={"slug": create_location.slug}))
    assert response.status_code == http.client.FOUND  # Redirect to login


def test_location_detail_view_authenticated(authenticated_client, create_location):
    response = authenticated_client.get(reverse("location_detail", kwargs={"slug": create_location.slug}))
    assert response.status_code == http.HTTPStatus.OK
    assert "pages/location_detail.html" in [t.name for t in response.templates]


def test_location_edit_view_unauthenticated(client, create_location):
    response = client.get(reverse("location_edit", kwargs={"slug": create_location.slug}))
    assert response.status_code == http.client.FOUND  # Redirect to login


def test_location_edit_view_authenticated_get(authenticated_client, create_location):
    response = authenticated_client.get(reverse("location_edit", kwargs={"slug": create_location.slug}))
    assert response.status_code == http.HTTPStatus.OK
    assert "pages/location_edit.html" in [t.name for t in response.templates]


def test_location_edit_view_authenticated_post(authenticated_client, create_location):
    data = {"name": "Updated Location", "slug": "test-location"}
    response = authenticated_client.post(reverse("location_edit", kwargs={"slug": create_location.slug}), data)
    create_location.refresh_from_db()
    assert response.status_code == http.client.FOUND  # Redirect after successful edit
    assert create_location.name == "Updated Location"
