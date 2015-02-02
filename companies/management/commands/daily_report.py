# -*- coding: utf-8 -*-
from django.conf import settings
from django.core.mail import send_mail
from django.core.management.base import BaseCommand

from companies.models import PurchasedCompany


class Command(BaseCommand):

    def handle(self, *args, **options):
        content = ''
        for purchased_company in PurchasedCompany.objects.filter(status='H'):
            latest_price = purchased_company.company.latest_price
            content += u'%s B:%s C:%s H:%s\n'%(purchased_company.company.name, purchased_company.buy_price, latest_price, purchased_company.highest_price)
        if content:
            send_mail(u'Daily Report', content, settings.EMAIL_HOST_USER,
                      [settings.SERVER_EMAIL])
