from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about", views.about, name="about"),
    path("location/", views.location_list, name="location_list"),
    path("location/view/<slug:slug>/", views.location_detail, name="location_detail"),
    path("location/create", views.location_list, name="location_create"),
    path("location/edit/<slug:slug>/", views.location_edit, name="location_edit"),
    path("location/delete/<slug:slug>/", views.location_list, name="location_delete"),
]
