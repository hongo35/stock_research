# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Finances',
            fields=[
                ('ccode', models.IntegerField(serialize=False, primary_key=True)),
                ('market_cap', models.FloatField()),
                ('shares_issued', models.FloatField()),
                ('dividend_yield', models.FloatField()),
                ('dividend_one', models.FloatField()),
                ('per', models.FloatField()),
                ('pbr', models.FloatField()),
                ('eps', models.FloatField()),
                ('bps', models.FloatField()),
                ('price_min', models.FloatField()),
                ('round_lot', models.FloatField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'finances',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
