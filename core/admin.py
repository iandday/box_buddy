from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from simple_history.admin import SimpleHistoryAdmin

from .models import URL
from .models import Box
from .models import File
from .models import Item


@admin.register(Box)
class BoxAdmin(SimpleHistoryAdmin, ImportExportModelAdmin):
    list_display = [
        "name",
        "slug",
        "created_by",
        "created_at",
        "updated_by",
        "updated_at",
        "is_active",
        "is_deleted",
    ]
    search_fields = ["name", "slug", "description"]
    list_filter = ["is_active", "is_deleted"]
    ordering = ["name"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Item)
class ItemAdmin(SimpleHistoryAdmin, ImportExportModelAdmin):
    list_display = [
        "name",
        "slug",
        "box",
        "quantity",
        "created_by",
        "created_at",
        "updated_by",
        "updated_at",
        "is_active",
        "is_deleted",
    ]
    search_fields = ["name", "slug", "description"]
    list_filter = ["is_active", "is_deleted", "box"]
    ordering = ["name"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(File)
class FileAdmin(SimpleHistoryAdmin, ImportExportModelAdmin):
    list_display = [
        "name",
        "slug",
        "item",
        "file",
        "created_by",
        "created_at",
        "updated_by",
        "updated_at",
        "is_active",
        "is_deleted",
    ]
    search_fields = ["name", "slug", "description"]
    list_filter = ["is_active", "is_deleted", "item", "box"]
    ordering = ["name"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(URL)
class URLAdmin(SimpleHistoryAdmin, ImportExportModelAdmin):
    list_display = [
        "name",
        "slug",
        "url",
        "item",
        "box",
        "created_by",
        "created_at",
        "updated_by",
        "updated_at",
        "is_active",
        "is_deleted",
    ]
    search_fields = ["name", "slug", "url", "description"]
    list_filter = ["is_active", "is_deleted", "item", "box"]
    ordering = ["name"]
    prepopulated_fields = {"slug": ("name",)}
