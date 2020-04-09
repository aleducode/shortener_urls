"""Cutter views."""

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.views.generic import FormView, View
from django.conf import settings

from url_shortener.cutter.models import Urls
from url_shortener.cutter.forms import UrlForm

from url_shortener.utils.general import get_short_code

class HomeView(View):
    pass

class RedirectOriginalView(View):
    """Rredurection to original url."""

    def dispatch(self, request, *args, **kwargs):
        """Handle request and validate url."""
        short_uri = kwargs.get('short_uri')
        import ipdb; ipdb.set_trace()
        url = get_object_or_404(Urls, short_uri=short_uri) # get object, if not        found return 404 error
        url.counter += 1
        url.save()
        return HttpResponseRedirect(url.http_url)


class ShortenerView(FormView):
    """Short url creator."""

    template_name = 'shortener.html'
    form_class = UrlForm

    def post(self, request, *args, **kwargs):
        """Form valid method handle and link generation."""
        form = self.get_form()
        shortened = 'Ocurrió un error'
        if form.is_valid():
            data = form.cleaned_data
            # Get dayta from form
            url = data.get('url', None)
            random_uri = get_short_code()
            Urls.objects.create(
                http_url=url,
                short_uri=random_uri
            )
            shortened = '{}/{}'.format(
                settings.SITE_URL,
                random_uri
            )

        return render(
            self.request,
            self.template_name,
            {
                'form': form,
                'shortened': shortened

            })
