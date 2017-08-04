# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-18 12:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote_box', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quote', models.CharField(max_length=500)),
                ('source', models.CharField(max_length=50)),
            ],
            options={
                'managed': False,
                'db_table': 'quotes',
                'ordering': ['source'],
            },
        ),
    ]
