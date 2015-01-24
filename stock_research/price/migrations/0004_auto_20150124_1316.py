# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0003_auto_20150123_0238'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='price',
            options={'managed': False},
        ),
    ]
