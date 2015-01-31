# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand

from companies.models import Company, SelectedCompany


class Command(BaseCommand):

    def handle(self, *args, **options):
        SelectedCompany.objects.all().delete()
        for company in Company.objects.all():
            initial_price = final_price =None
            good = True
            for stock in company.stock_set.order_by('-created_at')[:5]:
                if stock.pricechange < 0:
                    good = False
                    break
                if not initial_price:
                    initial_price = stock.trade
                final_price = stock.trade
            if good and initial_price and (final_price-initial_price)/initial_price >= 0.1:
                SelectedCompany(company=company).save()
