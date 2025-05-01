from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about", views.about, name="about"),
    path("location/", views.location_list, name="location_list"),
    path("location/view/<slug:slug>/", views.location_detail, name="location_detail"),
    path("location/create", views.location_create, name="location_create"),
    path("location/edit/<slug:slug>/", views.location_edit, name="location_edit"),
    path("location/delete/<slug:slug>/", views.location_list, name="location_delete"),
    path("box/", views.box_list, name="box_list"),
    path("box/view/<slug:slug>/", views.box_detail, name="box_detail"),
    path("box/create", views.box_create, name="box_create"),
    path("box/edit/<slug:slug>/", views.box_edit, name="box_edit"),
    path("box/delete/<slug:slug>/", views.box_list, name="box_delete"),
]
