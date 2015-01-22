# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0002_auto_20150122_0221'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='price',
            name='id',
        ),
        migrations.AlterField(
            model_name='price',
            name='ccode',
            field=models.IntegerField(serialize=False, primary_key=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='price',
            name='open',
            field=models.DecimalField(max_digits=10, decimal_places=2),
            preserve_default=True,
        ),
    ]
