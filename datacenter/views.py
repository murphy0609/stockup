# coding=utf-8
from django.shortcuts import render

# Create your views here.
from datacenter.models import StockData, StockCurrData


# 创建股票历史数据
def create_stock_data(stockname, stockcode, o, h, l, c, v, a, d5, d10, d20, d30, d50, d200):
    StockData(stockname=stockname, stockcode=stockcode, openV=o, highV=h, lowV=l, closeV=c,
              volume=v, adjclose=a, d5=d5, d10=d10, d20=d20, d30=d30, d50=d50, d200=d200).save()


# 创建股票当前数据
def create_stock_curr_data(stockname, stockcode, o, n, h, l, u, r, v, m, t):
    StockCurrData(stockname=stockname, stockcode=stockcode, openV=o, currV=n, highV=h, lowV=l,
                  upperV=u, range=r, volume=v, money=m, updatetime=t).save()
