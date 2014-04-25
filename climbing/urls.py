from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.conf import settings
from django.views.generic import dates
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from climbing.views import homepage, my_image, about
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'climbing.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', homepage),
    url(r'^image/', my_image),
    url(r'^about/$', about),
    url(r'^logbook/', include('logbook.urls', namespace="logbook")),
)
