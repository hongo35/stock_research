# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('ccode', models.IntegerField(serialize=False, primary_key=True)),
                ('industory_code', models.IntegerField()),
                ('industory_name', models.CharField(max_length=31)),
                ('market', models.CharField(max_length=31)),
                ('name', models.CharField(max_length=255)),
                ('info', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'brands',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
