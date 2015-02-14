# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.CharField(max_length=127, serialize=False, primary_key=True)),
                ('subject', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=1023)),
                ('source', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'articles',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
