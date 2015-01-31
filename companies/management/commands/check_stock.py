# -*- coding: utf-8 -*-
from django.conf import settings
from django.core.mail import send_mail
from django.core.management.base import BaseCommand

from companies.models import PurchasedCompany


class Command(BaseCommand):

    def handle(self, *args, **options):
        for purchased_company in PurchasedCompany.objects.filter(status='H'):
            latest_price = purchased_company.company.latest_price
            highest_price = purchased_company.highest_price

            if (highest_price-latest_price)/highest_price >= 0.13:
                send_mail(u'%s warning'%purchased_company.company.name,
                          u'B:%s C:%s H:%s'%(purchased_company.buy_price, latest_price, highest_price),
                          settings.EMAIL_HOST_USER, [settings.SERVER_EMAIL])

            if latest_price > highest_price:
                purchased_company.highest_price = latest_price
                purchased_company.save()
