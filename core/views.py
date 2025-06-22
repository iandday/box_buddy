from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render

from core.forms import BoxForm
from core.forms import ItemForm
from core.models import URL
from core.models import Box
from core.models import File
from core.models import Item
from users.forms import UserSettingsForm
from users.models import User


@login_required
def home(request: HttpRequest) -> HttpResponse:
    parents = (
        Box.objects.filter(is_active=True, is_deleted=False, parent=None)
        .annotate(child_count=Count("children"))
        .order_by("-view_count")
    )

    return render(request, "pages/home.html", {"parents": parents})


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
def box_list(request: HttpRequest) -> HttpResponse:
    if parent_slug := request.GET.get("parent"):
        parent = get_object_or_404(Box, slug=parent_slug, is_active=True, is_deleted=False)
        boxes = Box.objects.filter(is_active=True, is_deleted=False, parent=parent).order_by("name")
    else:
        boxes = Box.objects.filter(is_active=True, is_deleted=False).order_by("name")
        parent = None
    return render(request, "list/box_list.html", {"boxes": boxes, "parent": parent})


@login_required
def box_detail(request: HttpRequest, slug) -> HttpResponse:
    box = get_object_or_404(Box, slug=slug)
    box.view_count += 1
    box.save(update_fields=["view_count"])
    items = Item.objects.filter(box=box, is_active=True).order_by("name")
    child_boxes = Box.objects.filter(parent=box, is_active=True, is_deleted=False).order_by("name")
    return render(request, "detail/box_detail.html", {"box": box, "items": items, "child_boxes": child_boxes})


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


@login_required
def box_delete(request: HttpRequest, slug) -> HttpResponse:
    box = get_object_or_404(Box, slug=slug)
    if request.method == "POST":
        box.is_deleted = True
        box.save(update_fields=["is_deleted"])
        return redirect("box_list")
    return render(request, "forms/obj_delete.html", {"box": box, "title": "Delete Box"})


@login_required
def item_list(request: HttpRequest) -> HttpResponse:
    items = Item.objects.filter(is_active=True, is_deleted=False).order_by("name")
    return render(request, "list/item_list.html", {"items": items})


@login_required
def item_detail(request: HttpRequest, slug) -> HttpResponse:
    item = get_object_or_404(Item, slug=slug)
    files = File.objects.filter(item=item, is_active=True).order_by("name")
    urls = URL.objects.filter(item=item, is_active=True).order_by("name")
    return render(
        request,
        "detail/item_detail.html",
        {
            "item": item,
            "files": files,
            "urls": urls,
        },
    )


@login_required
def item_edit(request: HttpRequest, slug) -> HttpResponse:
    item = get_object_or_404(Item, slug=slug)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.instance.updated_by = request.user
            form.save()
            return redirect("item_detail", slug=item.slug)
    else:
        form = BoxForm(instance=item)
    return render(request, "forms/obj_create_edit.html", {"form": form, "item": item, "title": "Update Item"})
