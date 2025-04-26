from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.template.response import TemplateResponse

from core.models import Location


def home(request) -> TemplateResponse:
    return TemplateResponse(request, "pages/home.html", {})


def about(request) -> TemplateResponse:
    return TemplateResponse(request, "pages/about.html", {})


def location_list(request):
    locations = Location.objects.all()
    return render(request, "pages/location_list.html", {"locations": locations})


def location_detail(request, slug):
    location = get_object_or_404(Location, slug=slug)
    return render(request, "pages/location_detail.html", {"location": location})
