# -*- coding: utf-8 -*-
from django.db import models

import requests


class Company(models.Model):
    name = models.CharField(max_length=128)
    symbol = models.CharField(max_length=8, db_index=True)
    code = models.CharField(max_length=16, db_index=True)

    @property
    def latest_price(self):
        return float(requests.get('http://hq.sinajs.cn/list=%s'%self.symbol).text.split(',')[3])


class Stock(models.Model):
    company = models.ForeignKey(Company)
    trade = models.FloatField()  # 最新价
    pricechange = models.FloatField()  # 涨跌额
    changepercent = models.FloatField()  # 涨跌幅
    buy = models.FloatField()  # 买入
    sell = models.FloatField()  # 卖出
    settlement = models.FloatField()  # 昨收
    open = models.FloatField()  # 今开
    high = models.FloatField()  # 最高
    low = models.FloatField()  # 最低
    volume = models.FloatField()  # 成交量（12259278手）
    amount = models.FloatField()  # 成交额（2375559.10万）
    created_at = models.DateField(auto_now_add=True, db_index=True)


class SelectedCompany(models.Model):
    """
    Selected company for each day.
    Auto empty the table daily.
    Only the company increase 10-15% in the past 4-5days will be selected.
    """
    company = models.ForeignKey(Company)
    created_at = models.DateField(auto_now_add=True)


class PurchasedCompany(models.Model):

    STATUS_CHOICES = (
        ('H', 'Hold'),
        ('S', 'Sold'),
    )

    company = models.ForeignKey(Company)
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default='H')
    buy_price = models.FloatField()
    highest_price = models.FloatField()
    result = models.FloatField(blank=True, null=True)
    sell_at = models.DateField(auto_now_add=True)
    buy_at = models.DateField(auto_now_add=True)
