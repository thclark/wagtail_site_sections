from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SiteSectionsAppConfig(AppConfig):
    name = 'wagtail_site_sections'
    label = 'wagtail_site_sections'
    verbose_name = _('Wagtail Site Sections')

    def ready(self):
        pass
