# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-26 09:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('uid', models.CharField(max_length=256, primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, max_length=256, null=True)),
                ('surname', models.CharField(blank=True, max_length=256, null=True)),
                ('last_active', models.DateTimeField(blank=True, null=True)),
                ('message_cnt', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]