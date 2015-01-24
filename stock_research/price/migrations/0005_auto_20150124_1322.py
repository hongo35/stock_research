# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0004_auto_20150124_1316'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='price',
            table='prices',
        ),
    ]
