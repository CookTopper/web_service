# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-30 18:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cooktopper', '0016_burner_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='SmokeSensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('smoke_level', models.IntegerField()),
            ],
        ),
    ]
