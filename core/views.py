from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render

from core.forms import LocationForm
from core.models import Location


def home(request) -> HttpResponse:
    return render(request, "pages/home.html", {})


def about(request) -> HttpResponse:
    return render(request, "pages/about.html", {})


@login_required
def location_list(request) -> HttpResponse:
    locations = Location.objects.all()
    return render(request, "list/location_list.html", {"locations": locations})


@login_required
def location_detail(request, slug) -> HttpResponse:
    location = get_object_or_404(Location, slug=slug)
    return render(request, "detail/location_detail.html", {"location": location})


@login_required
def location_create(request) -> HttpResponse:
    if request.method == "POST":
        form = LocationForm(request.POST)
        if form.is_valid():
            form.instance.created_by = request.user
            location = form.save()
            return redirect("location_detail", slug=location.slug)
    else:
        form = LocationForm()
    return render(request, "forms/obj_create_edit.html", {"form": form, "title": "Create Location"})


@login_required
def location_edit(request, slug) -> HttpResponse:
    location = get_object_or_404(Location, slug=slug)
    if request.method == "POST":
        form = LocationForm(request.POST, instance=location)
        if form.is_valid():
            form.instance.updated_by = request.user
            form.save()
            return redirect("location_detail", slug=location.slug)
    else:
        form = LocationForm(instance=location)
    return render(
        request, "forms/obj_create_edit.html", {"form": form, "location": location, "title": "Update Location"}
    )
