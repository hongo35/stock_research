# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ccode', models.IntegerField(verbose_name=b'ccode')),
                ('date', models.DateField()),
                ('open', models.DecimalField(max_digits=10, decimal_places=2)),
                ('high', models.DecimalField(max_digits=10, decimal_places=2)),
                ('low', models.DecimalField(max_digits=10, decimal_places=2)),
                ('close', models.DecimalField(max_digits=10, decimal_places=2)),
                ('volume', models.DecimalField(max_digits=10, decimal_places=2)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'price',
            },
            bases=(models.Model,),
        ),
    ]
