"""Cutter serializer."""

# Django Rest Framework
from rest_framework import serializers

# Model
from url_shortener.cutter.models import (
    Urls
)
from url_shortener.utils.general import get_short_code


class ShortUrlSerializer(serializers.ModelSerializer):
    """Lead model Serializer."""

    shortened_url = serializers.SerializerMethodField()

    class Meta:

        model = Urls
        fields = (
            'shortened_url',
            'http_url',
            'created'
        )
        read_only = (
            'created'
        )
    
    def get_shortened_url(self, obj):
        """Return shorted url."""
        return obj.shorted_ur


class CreateShortUrlSerializer(serializers.Serializer):
    """Add Shortened serializer."""

    url_to_short = serializers.URLField()

    def create(self, data):
        """Create Shortened."""
        # Clean values
        url = data.get('url_to_short')
        random_uri = get_short_code()
        shortened_obj = Urls.objects.create(
            http_url=url,
            short_uri=random_uri
        )
        return shortened_obj
