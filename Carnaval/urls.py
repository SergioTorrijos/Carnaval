#encoding:utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'main.views.index'),
    url(r'^populateLetras', 'main.views.populateDBLetras'),
    url(r'^populateNoticias', 'main.views.populateDBNoticias'),
    url(r'^entrenarDatos', 'main.views.entrenarDatos'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

