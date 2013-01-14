from django.conf.urls import patterns, include, url
from app.api import NeumaticoResource

from django.contrib import admin
admin.autodiscover()

neumatico_resource = NeumaticoResource()

urlpatterns = patterns('',
    # Examples:
    url(r'^contacto/$','app.views.contacto'),
    # url(r'^$', 'hankook.views.home', name='home'),
    # url(r'^hankook/', include('hankook.foo.urls')),
     # url(r'^search-form/$', 'app.views.search_form'),
     # url (r'^contact/thankyou/', 'app.views.thankyou'),
     # url(r'^contact/', 'app.views.contactview'),
     url(r'^$', 'app.views.index'),

     url(r'^productos/$', 'app.views.productos'),

     url(r'^api/', include(neumatico_resource.urls)),
     # url(r'^search/$', 'app.views.search'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

