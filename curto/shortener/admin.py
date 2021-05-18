from django.contrib import admin
from curto.shortener.models import UrlRedirect


@admin.register(UrlRedirect)
class UrlRedirectAdmin(admin.ModelAdmin):
    list_display = ('target', 'slug', 'created_at', 'updated_at')
