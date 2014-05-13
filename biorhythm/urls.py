from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'biorhythm.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r'^makewave/(?P<month>[0-9]{0,2})/(?P<day>[0-9]{0,2})/(?P<year>[0-9]{4})/$', 'makewave.views.makewave'),
)
