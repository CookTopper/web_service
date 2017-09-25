# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cooktopper', '0002_auto_20170925_1350'),
    ]

    operations = [
        migrations.RenameField(
            model_name='burner',
            old_name='burner_state_id',
            new_name='burner_state',
        ),
        migrations.RenameField(
            model_name='burner',
            old_name='stove_id',
            new_name='stove',
        ),
        migrations.RenameField(
            model_name='burner',
            old_name='temperature_id',
            new_name='temperature',
        ),
        migrations.RenameField(
            model_name='pan',
            old_name='pan_state_id',
            new_name='pan_state',
        ),
        migrations.RenameField(
            model_name='programming',
            old_name='burner_id',
            new_name='burner',
        ),
        migrations.RenameField(
            model_name='programmingdetails',
            old_name='programming_type_id',
            new_name='programming_type',
        ),
        migrations.RenameField(
            model_name='programmingdetails',
            old_name='temperature_id',
            new_name='temperature',
        ),
    ]
