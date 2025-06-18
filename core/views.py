from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render

from core.forms import BoxForm
from core.forms import LocationForm
from core.models import Box
from core.models import Location
from users.forms import UserSettingsForm
from users.models import User


@login_required
def home(request: HttpRequest) -> HttpResponse:
    return render(request, "pages/home.html", {})


@login_required
def about(request: HttpRequest) -> HttpResponse:
    return render(request, "pages/about.html", {})


@login_required
def settings(request: HttpRequest) -> HttpResponse:
    # get user instance
    if request.method == "GET":
        user = User.objects.get(id=request.user.pk)
        form = UserSettingsForm(instance=user)
        return render(request, "pages/settings.html", {"user": user, "form": form})
        # render settings page with user instance
    if request.method == "POST":
        user = User.objects.get(id=request.user.pk)
        form = UserSettingsForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            # update request user instance
            request.user = form.instance
        # redirect to settings page with updated user instance
        return redirect("settings")
    return render(request, "pages/settings.html", {"user": request.user})


@login_required
def location_list(request: HttpRequest) -> HttpResponse:
    locations = Location.objects.all()
    return render(request, "list/location_list.html", {"locations": locations})


@login_required
def location_detail(request: HttpRequest, slug) -> HttpResponse:
    location = get_object_or_404(Location, slug=slug)
    return render(request, "detail/location_detail.html", {"location": location})


@login_required
def location_create(request: HttpRequest) -> HttpResponse:
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
def location_edit(request: HttpRequest, slug) -> HttpResponse:
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
def box_list(request: HttpRequest) -> HttpResponse:
    boxes = Box.objects.all()
    return render(request, "list/box_list.html", {"boxes": boxes})


@login_required
def box_detail(request: HttpRequest, slug) -> HttpResponse:
    box = get_object_or_404(Box, slug=slug)
    return render(request, "detail/box_detail.html", {"box": box})


@login_required
def box_create(request: HttpRequest) -> HttpResponse:
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
def box_edit(request: HttpRequest, slug) -> HttpResponse:
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
