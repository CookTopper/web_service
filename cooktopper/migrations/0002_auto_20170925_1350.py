# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cooktopper', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Burner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='BurnerState',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Pan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=45)),
                ('temperature', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PanState',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Programming',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('burner_id', models.ForeignKey(to='cooktopper.Burner')),
            ],
        ),
        migrations.CreateModel(
            name='ProgrammingDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('programmed_hour', models.CharField(max_length=45)),
                ('expected_duration', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ProgrammingType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Shortcut',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=45)),
                ('programming_details', models.ForeignKey(to='cooktopper.ProgrammingDetails')),
            ],
        ),
        migrations.CreateModel(
            name='Temperature',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=45)),
            ],
        ),
        migrations.AddField(
            model_name='programmingdetails',
            name='programming_type_id',
            field=models.ForeignKey(to='cooktopper.ProgrammingType'),
        ),
        migrations.AddField(
            model_name='programmingdetails',
            name='temperature_id',
            field=models.ForeignKey(to='cooktopper.Temperature'),
        ),
        migrations.AddField(
            model_name='programming',
            name='programming_details',
            field=models.ForeignKey(to='cooktopper.ProgrammingDetails'),
        ),
        migrations.AddField(
            model_name='pan',
            name='pan_state_id',
            field=models.ForeignKey(to='cooktopper.PanState'),
        ),
        migrations.AddField(
            model_name='burner',
            name='burner_state_id',
            field=models.ForeignKey(to='cooktopper.BurnerState'),
        ),
        migrations.AddField(
            model_name='burner',
            name='stove_id',
            field=models.ForeignKey(to='cooktopper.Stove'),
        ),
        migrations.AddField(
            model_name='burner',
            name='temperature_id',
            field=models.ForeignKey(to='cooktopper.Temperature'),
        ),
    ]
