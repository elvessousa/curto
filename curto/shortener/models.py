from django.db import models


class UrlRedirect(models.Model):
    """ Redirection URLs table """

    target = models.URLField(max_length=512)
    slug = models.SlugField(max_length=128, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.target} -> {self.slug}'


class UrlLog(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    origin = models.URLField(max_length=512, null=True, blank=True)
    user_agent = models.CharField(max_length=512, null=True, blank=True)
    host = models.CharField(max_length=512, null=True, blank=True)
    ip = models.GenericIPAddressField(null=True, blank=True)
    url_redirect = models.ForeignKey(
        UrlRedirect, models.DO_NOTHING, related_name='logs')
