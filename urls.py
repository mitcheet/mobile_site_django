from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^librware/', include('librware.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     (r'^admin/', include(admin.site.urls)),
     (r'^index/$', 'librware.librware_mobile.views.index'),
     (r'^site/(?P<library_id>\d+)/$', 'librware.librware_mobile.views.detail'),
     (r'^feed/(?P<feed_id>\d+)/$', 'librware.librware_mobile.views.feed'),
     #(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/Users/mitcheet/librware/static'}),
     #(r'^search/(?P<search_terms>\w+)/$', 'librware.librware_mobile.views.search'), 
      (r'^search/', 'librware.librware_mobile.views.search'),
)
