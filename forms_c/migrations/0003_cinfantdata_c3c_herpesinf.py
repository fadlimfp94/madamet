# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-09-16 11:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms_c', '0002_auto_20170916_1410'),
    ]

    operations = [
        migrations.AddField(
            model_name='cinfantdata',
            name='c3c_herpesinf',
            field=models.NullBooleanField(default=False),
        ),
    ]