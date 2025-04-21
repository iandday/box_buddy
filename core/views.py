from django.template.response import TemplateResponse


def home(request) -> TemplateResponse:
    return TemplateResponse(request, "pages/home.html", {})


def about(request) -> TemplateResponse:
    return TemplateResponse(request, "pages/about.html", {})
