# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-18 05:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.FloatField()),
                ('name', models.CharField(max_length=250)),
                ('availibility', models.BooleanField(default=True)),
                ('outLength', models.IntegerField(default=0)),
            ],
        ),
    ]
