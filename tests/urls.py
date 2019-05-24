from django.conf.urls import include, url
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls


# This is the URL Config for the test server
urlpatterns = [
    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'', include(wagtail_urls)),
]
