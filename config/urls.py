"""Urls shortener."""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    # # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    # # User management
    path("", include("url_shortener.cutter.urls", namespace="cutter")),
    # path("accounts/", include("allauth.urls")),
    # Your stuff: custom urls includes go here
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# API URLS
urlpatterns += [
    # # API base url
    # path("api/", include("config.api_router")),
    # # DRF auth token
    # path("auth-token/", obtain_auth_token),
]
