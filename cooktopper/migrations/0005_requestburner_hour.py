# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-28 19:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cooktopper', '0004_requestburner'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestburner',
            name='hour',
            field=models.CharField(default=1234, max_length=45),
            preserve_default=False,
        ),
    ]