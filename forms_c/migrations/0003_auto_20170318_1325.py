# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-18 06:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms_c', '0002_auto_20170318_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cmother',
            name='c1m_swab_date',
            field=models.DateField(null=True),
        ),
    ]