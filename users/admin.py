# mypy: disable-error-code="misc, type-arg"

from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from simple_history.admin import SimpleHistoryAdmin

from .models import User


@admin.register(User)
class UserAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    list_display = ["email", "first_name", "last_name", "is_active", "is_admin"]
    search_fields = ["email, first_name", "last_name"]
    list_filter = ["is_active", "is_admin"]
    ordering = ["email"]
    list_per_page = 20
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name")}),
        ("Permissions", {"fields": ("is_active", "is_admin")}),
    )
    add_fieldsets = (
        (None, {"classes": ("wide",), "fields": ("email", "password1", "password2")}),
        ("Personal info", {"fields": ("first_name", "last_name")}),
        ("Permissions", {"fields": ("is_active", "is_admin")}),
    )
