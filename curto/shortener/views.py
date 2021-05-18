from django.shortcuts import render, redirect
from django.http import HttpResponse

from curto.shortener.models import UrlRedirect


def redirection(request, slug):
    """ Redirection """

    url_redirect = UrlRedirect.objects.get(slug=slug)

    if slug != 'admin/':
        return redirect(url_redirect.target)
