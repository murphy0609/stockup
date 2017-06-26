# coding=utf-8
from django.db import models


# Create your models here.

class StockData(models.Model):
    stockname = models.CharField(verbose_name=u'股票名称', default=None, max_length=50)
    stockcode = models.CharField(verbose_name=u'股票代码', default=None, max_length=10)
    openV = models.FloatField(verbose_name=u'开盘', default=0.0)
    highV = models.FloatField(verbose_name=u'最高', default=0.0)
    lowV = models.FloatField(verbose_name=u'最低', default=0.0)
    closeV = models.FloatField(verbose_name=u'收盘', default=0.0)
    volume = models.FloatField(verbose_name=u'成交量', default=0.0)
    adjclose = models.FloatField(verbose_name=u'已调整收盘价', default=0.0)
    d5 = models.FloatField(verbose_name=u'5日均线', default=0.0, blank=True)
    d10 = models.FloatField(verbose_name=u'10日均线', default=0.0, blank=True)
    d20 = models.FloatField(verbose_name=u'20日均线', default=0.0, blank=True)
    d30 = models.FloatField(verbose_name=u'30日均线', default=0.0, blank=True)
    d50 = models.FloatField(verbose_name=u'50日均线', default=0.0, blank=True)
    d200 = models.FloatField(verbose_name=u'200日均线', default=0.0, blank=True)

    class Meta:
        verbose_name_plural = u'股票历史数据'


class StockCurrData(models.Model):
    stockname = models.CharField(verbose_name=u'股票名称', default=None, max_length=50)
    stockcode = models.CharField(verbose_name=u'股票代码', default=None, max_length=10)
    openV = models.FloatField(verbose_name=u'开盘', default=0.0)
    currV = models.FloatField(verbose_name=u'最新', default=0.0)
    highV = models.FloatField(verbose_name=u'最高', default=0.0)
    lowV = models.FloatField(verbose_name=u'最低', default=0.0)
    upperV = models.FloatField(verbose_name=u'涨跌', default=0.0)
    range = models.FloatField(verbose_name=u'幅度', default=0.0)
    volume = models.FloatField(verbose_name=u'总手(万)', default=0.0)
    money = models.FloatField(verbose_name=u'金额（亿）', default=0.0)
    updatetime = models.DateTimeField(verbose_name=u'更新时间', default='1990-01-01 00:00:00')

    class Meta:
        verbose_name_plural = u'股票当前数据'
