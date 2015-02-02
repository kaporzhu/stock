from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import RedirectView


urlpatterns = patterns('',
    url(r'^$', RedirectView.as_view(permanent=False, url='/companies/')),
    url(r'^companies/', include('companies.urls', 'companies', 'companies')),

    url(r'^admin/', include(admin.site.urls)),
)
