from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from .models import User
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from simple_history.admin import SimpleHistoryAdmin


@admin.register(User)
class UserAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    list_display = ["email", "name", "is_superuser"]
    search_fields = ["name"]