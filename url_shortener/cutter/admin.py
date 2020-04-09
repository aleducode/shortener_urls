"""Admin Cutter."""

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Models
from url_shortener.cutter.models import User, Urls

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    pass


@admin.register(Urls)
class UrlsAdmin(admin.ModelAdmin):
    """Urls Admin."""

    list_display = ['http_url', 'short_uri']


