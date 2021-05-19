from django.shortcuts import render, redirect
from django.http import HttpResponse

from curto.shortener.models import UrlRedirect


def redirection(request, slug):
    """ Redirection """

    url_redirect = UrlRedirect.objects.get(slug=slug)

    return redirect(url_redirect.target)


def reports(request, slug):
    """ Shows shortened link report on screen """

    url_redirect = UrlRedirect.objects.get(slug=slug)
    site_url = request.build_absolute_uri(f'/{slug}')
    context = {
        'reduce': url_redirect,
        'url': site_url
    }

    return render(request, 'shortener/reports.html', context)
