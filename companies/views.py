# -*- coding: utf-8 -*-
from datetime import datetime

from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView

from braces.views import SuperuserRequiredMixin

from .forms import PurchasedCompanyForm
from .models import Company, SelectedCompany, PurchasedCompany


class CompanyListView(SuperuserRequiredMixin, ListView):
    model = Company
    paginate_by = 100


class SelectedCompanyListView(SuperuserRequiredMixin, ListView):
    model = SelectedCompany


class PurchasedCompanyListView(SuperuserRequiredMixin, ListView):
    model = PurchasedCompany


class PurchasedCompanyCreateView(SuperuserRequiredMixin, CreateView):
    model = PurchasedCompany
    form_class = PurchasedCompanyForm
    success_url = reverse_lazy('companies:purchased_company_list')

    def form_valid(self, form):
        purchased_company = form.save(commit=False)
        purchased_company.company = Company.objects.get(pk=self.request.GET['company'])
        purchased_company.highest_price = purchased_company.buy_price
        self.object = purchased_company
        return super(PurchasedCompanyCreateView, self).form_valid(form)


class PurchasedCompanyUpdateView(SuperuserRequiredMixin, UpdateView):
    model = PurchasedCompany
    form_class = PurchasedCompanyForm
    success_url = reverse_lazy('companies:purchased_company_list')

    def form_valid(self, form):
        if self.object.status == 'S' and PurchasedCompany.objects.get(pk=self.object.id).status == 'H':
            self.object.sell_at = datetime.now().date()
        return super(PurchasedCompanyUpdateView, self).form_valid(form)
