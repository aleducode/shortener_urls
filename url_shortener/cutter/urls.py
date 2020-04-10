"""Cutter urls."""
# Django
from django.urls import path, re_path, include

# Django Rest Freamework
from rest_framework.routers import DefaultRouter

# Views
from url_shortener.cutter import views as cutter_views

router = DefaultRouter()
router.register(r'api/shortener', cutter_views.CutterViewset, basename='api')

app_name = "cutter"
urlpatterns = [
    path('', include(router.urls)),
    re_path(
        route=r'^(?P<short_uri>\w{6})$',
        view=cutter_views.RedirectOriginalView.as_view(),
        name='redirect_original'
    )
]
