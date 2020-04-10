"""Urls shortener."""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path

# Django Rest Framework
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Shortener url API",
        default_version='v1',
        description="Open source shortener url api.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    re_path(r'^$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path(settings.ADMIN_URL, admin.site.urls),
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
