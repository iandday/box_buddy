from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render

from core.forms import BoxForm
from core.forms import LocationForm
from core.models import Box
from core.models import Location


def home(request) -> HttpResponse:
    return render(request, "pages/home.html", {})


def about(request) -> HttpResponse:
    return render(request, "pages/about.html", {})


@login_required
def settings(request) -> HttpResponse:
    return render(request, "pages/settings.html", {})


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


@login_required
def box_list(request) -> HttpResponse:
    boxes = Box.objects.all()
    return render(request, "list/box_list.html", {"boxes": boxes})


@login_required
def box_detail(request, slug) -> HttpResponse:
    box = get_object_or_404(Box, slug=slug)
    return render(request, "detail/box_detail.html", {"box": box})


@login_required
def box_create(request) -> HttpResponse:
    if request.method == "POST":
        form = BoxForm(request.POST)
        if form.is_valid():
            form.instance.created_by = request.user
            box = form.save()
            return redirect("box_detail", slug=box.slug)
    else:
        form = BoxForm()
    return render(request, "forms/obj_create_edit.html", {"form": form, "title": "Create Box"})


@login_required
def box_edit(request, slug) -> HttpResponse:
    box = get_object_or_404(Box, slug=slug)
    if request.method == "POST":
        form = BoxForm(request.POST, instance=box)
        if form.is_valid():
            form.instance.updated_by = request.user
            form.save()
            return redirect("box_detail", slug=box.slug)
    else:
        form = BoxForm(instance=box)
    return render(request, "forms/obj_create_edit.html", {"form": form, "box": box, "title": "Update Box"})
