# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-03 12:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms_a', '0002_auto_20170116_0134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='a5prepregnancysmoking',
            name='a5f_father_smoke_frequency',
            field=models.CharField(choices=[('1', 'Daily'), ('2', 'Weekly'), ('3', 'Monthly'), ('0', 'Never')], default='', max_length=1),
        ),
    ]
