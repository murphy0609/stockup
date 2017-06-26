# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datacenter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockCurrData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stockname', models.CharField(default=None, max_length=50, verbose_name='\u80a1\u7968\u540d\u79f0')),
                ('stockcode', models.CharField(default=None, max_length=10, verbose_name='\u80a1\u7968\u4ee3\u7801')),
                ('openV', models.FloatField(default=0.0, verbose_name='\u5f00\u76d8')),
                ('currV', models.FloatField(default=0.0, verbose_name='\u6700\u65b0')),
                ('highV', models.FloatField(default=0.0, verbose_name='\u6700\u9ad8')),
                ('lowV', models.FloatField(default=0.0, verbose_name='\u6700\u4f4e')),
                ('upperV', models.FloatField(default=0.0, verbose_name='\u6da8\u8dcc')),
                ('range', models.FloatField(default=0.0, verbose_name='\u5e45\u5ea6')),
                ('volume', models.FloatField(default=0.0, verbose_name='\u603b\u624b(\u4e07)')),
                ('money', models.FloatField(default=0.0, verbose_name='\u91d1\u989d\uff08\u4ebf\uff09')),
                ('updatetime', models.DateTimeField(default=b'1990-01-01 00:00:00', verbose_name='\u66f4\u65b0\u65f6\u95f4')),
            ],
            options={
                'verbose_name_plural': '\u80a1\u7968\u6570\u636e',
            },
        ),
        migrations.AddField(
            model_name='stockdata',
            name='stockcode',
            field=models.CharField(default=None, max_length=10, verbose_name='\u80a1\u7968\u4ee3\u7801'),
        ),
        migrations.AddField(
            model_name='stockdata',
            name='stockname',
            field=models.CharField(default=None, max_length=50, verbose_name='\u80a1\u7968\u540d\u79f0'),
        ),
    ]
