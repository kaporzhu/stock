# -*- coding: utf-8 -*-
import json
import re
from datetime import datetime

from django.core.management.base import BaseCommand

import requests

from companies.models import Company, Stock


class Command(BaseCommand):
    url = 'http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeData?node=%s&num=10000'
    nodes = ['hs_a', 'hs_b', 'sz_a', 'sz_b']

    def handle(self, *args, **options):
        for node in self.nodes:
            content = re.sub('([,\{\[])(\w*?)\:', '\g<1>"\g<2>":', requests.get(self.url%node).text)
            for data in json.loads(content):
                # get or create company
                company, created = Company.objects.get_or_create(symbol=data['symbol'])
                if created:
                    company.code = data['code']
                    company.name = data['name']
                    company.save()

                # save stock info
                try:
                    Stock.objects.get(company=company, created_at=datetime.now().date())
                except Stock.DoesNotExist:
                    # check if the last stock is the same of current one.
                    # exclude the weekend and vacation
                    last_stock = Stock.objects.filter(company=company).order_by('-created_at').first()
                    if last_stock and last_stock.pricechange == data['pricechange'] and last_stock.trade == data['trade']:
                        break
                    stock = Stock(company=company)
                    for field in ['trade', 'pricechange', 'changepercent',
                            'buy', 'sell', 'settlement', 'open', 'high', 'low',
                            'volume', 'amount']:
                        setattr(stock, field, float(data[field]))
                    stock.save()
