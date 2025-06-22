from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("settings/", views.settings, name="settings"),
    path("box/", views.box_list, name="box_list"),
    path("box/view/<slug:slug>/", views.box_detail, name="box_detail"),
    path("box/create/", views.box_create, name="box_create"),
    path("box/edit/<slug:slug>/", views.box_edit, name="box_edit"),
    path("box/delete/<slug:slug>/", views.box_delete, name="box_delete"),
    path("item/", views.item_list, name="item_list"),
    path("item/create/", views.item_create, name="item_create"),
    path("item/view/<slug:slug>/", views.item_detail, name="item_detail"),
    path("item/edit/<slug:slug>/", views.item_edit, name="item_edit"),
]
