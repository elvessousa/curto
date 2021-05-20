from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Count
from django.db.models.functions import TruncDate

from curto.shortener.models import UrlRedirect, UrlLog


def redirection(request, slug):
    """ Redirection """

    url_redirect = UrlRedirect.objects.get(slug=slug)

    # Add redirection info to UrlLog
    UrlLog.objects.create(
        origin=request.META.get('HTTP_REFERER'),
        user_agent=request.META.get('HTTP_USER_AGENT'),
        host=request.META.get('HTTP_HOST'),
        ip=request.META.get('REMOTE_ADDR'),
        url_redirect=url_redirect
    )

    return redirect(url_redirect.target)


def reports(request, slug):
    """ Shows shortened link report on screen """

    url_redirect = UrlRedirect.objects.get(slug=slug)
    site_url = request.build_absolute_uri(f'/{slug}')

    redirects_by_date = list(
        UrlRedirect.objects.filter(
            slug=slug
        ).annotate(
            date=TruncDate('logs__created_at')
        ).annotate(
            clicks=Count('date')
        ).order_by('date')
    )

    context = {
        'reduce': url_redirect,
        'url': site_url,
        'redirects_by_date': redirects_by_date,
        'total_clicks': sum(r.clicks for r in redirects_by_date)
    }

    return render(request, 'shortener/reports.html', context)
