# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-09-17 01:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms_d', '0007_auto_20170917_0831'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='d5infantbiological',
            name='d5c_buccal_swab',
        ),
        migrations.RemoveField(
            model_name='d5infantbiological',
            name='d5c_buccal_swab_date',
        ),
        migrations.RemoveField(
            model_name='d5infantbiological2',
            name='d5c_buccal_swab',
        ),
        migrations.RemoveField(
            model_name='d5infantbiological2',
            name='d5c_buccal_swab_date',
        ),
        migrations.RemoveField(
            model_name='d5infantbiological3',
            name='d5c_buccal_swab',
        ),
        migrations.RemoveField(
            model_name='d5infantbiological3',
            name='d5c_buccal_swab_date',
        ),
        migrations.RemoveField(
            model_name='d5infantbiological4',
            name='d5c_buccal_swab',
        ),
        migrations.RemoveField(
            model_name='d5infantbiological4',
            name='d5c_buccal_swab_date',
        ),
    ]
