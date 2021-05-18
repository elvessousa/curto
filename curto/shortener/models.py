from django.db import models


class UrlRedirect(models.Model):
    """ Redirection URLs table """

    target = models.URLField(max_length=512)
    slug = models.SlugField(max_length=128, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.target} -> {self.slug}'
