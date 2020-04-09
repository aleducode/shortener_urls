"""Cutter app."""

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class CutterConfig(AppConfig):
    name = "url_shortener.cutter"
    verbose_name = _("Cutter")
