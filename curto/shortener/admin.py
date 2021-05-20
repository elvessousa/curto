from django.contrib import admin
from curto.shortener.models import UrlRedirect, UrlLog


@admin.register(UrlRedirect)
class UrlRedirectAdmin(admin.ModelAdmin):
    """ Shows and creates redirections on Admin """
    list_display = ('target', 'slug', 'created_at', 'updated_at')


@admin.register(UrlLog)
class UrlLogAdmin(admin.ModelAdmin):
    """ Shows data from each redirection access """
    list_display = ('origin', 'created_at', 'user_agent',
                    'host', 'ip', 'url_redirect')

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
