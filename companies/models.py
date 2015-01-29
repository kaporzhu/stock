# -*- coding: utf-8 -*-
from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=128)
    symbol = models.CharField(max_length=8, db_index=True)
    code = models.CharField(max_length=16, db_index=True)


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
