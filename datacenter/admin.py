# coding=utf-8
from django.contrib import admin

# Register your models here.
from datacenter.models import StockData, StockCurrData


@admin.register(StockData)
class StockDataAdmin(admin.ModelAdmin):
    pass


@admin.register(StockCurrData)
class StockCurrDataAdmin(admin.ModelAdmin):
    list_display = ['stockname', 'stockcode', 'openV', 'currV', 'highV', 'lowV', 'upperV',
                    'range', 'volume', 'money', 'updatetime']
    pass
