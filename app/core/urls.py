from django.views.generic import TemplateView
from django.urls import include, path
from . import views
urlpatterns = [
    path("", views.home, name="home"),
    path(
        "about/",
        TemplateView.as_view(template_name="pages/about.html"),
        name="about",
    ),

]