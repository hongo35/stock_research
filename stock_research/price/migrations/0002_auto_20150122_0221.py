# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='open',
            field=models.DecimalField(max_digits=10, decimal_places=1),
            preserve_default=True,
        ),
    ]
