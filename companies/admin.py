# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Company, Stock, SelectedCompany, PurchasedCompany


admin.site.register(Company)
admin.site.register(Stock)
admin.site.register(SelectedCompany)
admin.site.register(PurchasedCompany)
