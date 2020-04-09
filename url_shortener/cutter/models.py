"""Cutter Models."""

from django.contrib.auth.models import AbstractUser
from django_extensions.db.models import TimeStampedModel
from django.db import models


class User(TimeStampedModel, AbstractUser):
    """User model.

    Extend from Django's Abstract User, change the username field
    to email and add some extra fields.
    """

    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': 'Ya existe un usuario con ese email.'
        }
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        """Return username."""
        return self.username

    def get_short_name(self):
        """Return username."""
        return self.username

    class Meta:
        """Meta class."""

        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"


class Urls(TimeStampedModel, models.Model):
    """Urls Models."""

    http_url = models.URLField(max_length=200)
    counter = models.IntegerField(default=0)
    short_uri = models.SlugField()

    class Meta:
        verbose_name = 'Url shortened'
        verbose_name_plural = 'Urls shortened'

    def __str__(self):
        """Return username."""
        return self.short_uri
