# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from .views import(
    CompanyListView, SelectedCompanyListView, PurchasedCompanyListView,
    PurchasedCompanyCreateView, PurchasedCompanyUpdateView
)


urlpatterns = patterns('',
    url(r'^$', CompanyListView.as_view(), name='list'),
    url(r'^selected/$', SelectedCompanyListView.as_view(), name='selected_company_list'),
    url(r'^purchased/$', PurchasedCompanyListView.as_view(), name='purchased_company_list'),
    url(r'^purchased/create/$', PurchasedCompanyCreateView.as_view(), name='create_purchased_company'),
    url(r'^purchased/(?P<pk>\d+)/update/$', PurchasedCompanyUpdateView.as_view(), name='update_purchased_company'),
)
