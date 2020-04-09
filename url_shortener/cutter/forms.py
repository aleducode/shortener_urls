"""Cutter forms."""

from django import forms


class UrlForm(forms.Form):

    url = forms.URLField(
        label='Url to short.'
    )
