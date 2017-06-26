# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StockData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('openV', models.FloatField(default=0.0, verbose_name='\u5f00\u76d8')),
                ('highV', models.FloatField(default=0.0, verbose_name='\u6700\u9ad8')),
                ('lowV', models.FloatField(default=0.0, verbose_name='\u6700\u4f4e')),
                ('closeV', models.FloatField(default=0.0, verbose_name='\u6536\u76d8')),
                ('volume', models.FloatField(default=0.0, verbose_name='\u6210\u4ea4\u91cf')),
                ('adjclose', models.FloatField(default=0.0, verbose_name='\u5df2\u8c03\u6574\u6536\u76d8\u4ef7')),
                ('d5', models.FloatField(default=0.0, verbose_name='5\u65e5\u5747\u7ebf', blank=True)),
                ('d10', models.FloatField(default=0.0, verbose_name='10\u65e5\u5747\u7ebf', blank=True)),
                ('d20', models.FloatField(default=0.0, verbose_name='20\u65e5\u5747\u7ebf', blank=True)),
                ('d30', models.FloatField(default=0.0, verbose_name='30\u65e5\u5747\u7ebf', blank=True)),
                ('d50', models.FloatField(default=0.0, verbose_name='50\u65e5\u5747\u7ebf', blank=True)),
                ('d200', models.FloatField(default=0.0, verbose_name='200\u65e5\u5747\u7ebf', blank=True)),
            ],
            options={
                'verbose_name_plural': '\u80a1\u7968\u6570\u636e',
            },
        ),
    ]
