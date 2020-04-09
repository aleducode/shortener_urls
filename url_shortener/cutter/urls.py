"""Cutter urls."""

from django.urls import path, re_path

# Views
from url_shortener.cutter import views as cutter_views

app_name = "cutter"
urlpatterns = [
    path(
        route='',
        view=cutter_views.HomeView.as_view(),
        name='home'
    ),
    re_path(
        route=r'^(?P<short_uri>\w{6})$',
        view=cutter_views.RedirectOriginalView.as_view(),
        name='redirect_original'
    ),
    path(
        route='makeshort/',
        view=cutter_views.ShortenerView.as_view(),
        name='makeshort'
    ),
]
