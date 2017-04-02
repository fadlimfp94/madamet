# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-30 01:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms_c', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cinfantdata',
            old_name='c3c_iterus',
            new_name='c3c_icterus',
        ),
        migrations.AlterField(
            model_name='cinfantdata',
            name='c3c_air_cpap',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='cinfantdata',
            name='c3c_air_intubation',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='cinfantdata',
            name='c3c_air_ippr',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='cinfantdata',
            name='c3c_cardiac_massage',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='cinfantdata',
            name='c3c_oxygen_cpap',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='cinfantdata',
            name='c3c_oxygen_intubation',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='cinfantdata',
            name='c3c_oxygen_ippr',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='cinfantdata',
            name='c3c_oxygen_therapy',
            field=models.BooleanField(default=False),
        ),
    ]