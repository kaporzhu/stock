# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand

from companies.models import Company, SelectedCompany


class Command(BaseCommand):

    def handle(self, *args, **options):
        SelectedCompany.objects.all().delete()
        for company in Company.objects.all():
            latest_price = oldest_price =None
            good = True
            for stock in company.stock_set.order_by('-created_at')[:5]:
                if stock.pricechange < 0:
                    good = False
                    break
                if not latest_price:
                    latest_price = stock.trade
                oldest_price = stock.trade
            if good and latest_price and oldest_price and (latest_price-oldest_price)/oldest_price >= 0.1:
                SelectedCompany(company=company).save()
