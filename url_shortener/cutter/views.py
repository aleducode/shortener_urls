"""Cutter views."""


from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import View

from rest_framework_api_key.permissions import HasAPIKey
from rest_framework import status, viewsets, mixins
from rest_framework.response import Response


from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from url_shortener.cutter.models import Urls

from url_shortener.cutter.serializers import (
    CreateShortUrlSerializer,
    ShortUrlSerializer
)


class CutterViewset(mixins.CreateModelMixin,
                    viewsets.GenericViewSet):
    """Cutter url view set.

    Handle cutter creation.
    """

    permission_classes = [HasAPIKey]

    def get_serializer_class(self):
        """Return serializer based on action."""
        if self.action == 'create':
            return CreateShortUrlSerializer
        return ShortUrlSerializer

    @swagger_auto_schema(responses={
        201: openapi.Response(
            'Short url response.',
            ShortUrlSerializer)
    })
    def create(self, request, *args, **kwargs):
        """Creation short url method."""
        serializer = self.get_serializer(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        url = serializer.save()
        lead_response = ShortUrlSerializer(url).data
        return Response(lead_response, status=status.HTTP_201_CREATED)


class RedirectOriginalView(View):
    """Rredurection to original url."""

    def dispatch(self, request, *args, **kwargs):
        """Handle request and validate url."""
        short_uri = kwargs.get('short_uri')
        url = get_object_or_404(Urls, short_uri=short_uri) # get object, if not        found return 404 error
        url.counter += 1
        url.save()
        return HttpResponseRedirect(url.http_url)
