# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-09-26 05:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms_b2', '0002_auto_20170925_2249'),
    ]

    operations = [
        migrations.RenameField(
            model_name='b2gestationalnutrition',
            old_name='b6m_other_duration',
            new_name='b6m_other_med',
        ),
        migrations.RenameField(
            model_name='b2gestationalnutrition',
            old_name='b6m_other',
            new_name='b6m_other_med_exist',
        ),
        migrations.RenameField(
            model_name='b2gestationalnutrition',
            old_name='b6m_other_routine',
            new_name='b6m_other_med_routine',
        ),
        migrations.AddField(
            model_name='b2gestationalnutrition',
            name='b6m_other_med_duration',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='b2currentsmookinghabits',
            name='b4m_notes',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='b2currentsmookinghabits',
            name='b4m_smoking_status',
            field=models.CharField(blank=True, choices=[('', ''), ('1', 'Smoker'), ('2', 'Ex-smoker'), ('0', 'Never smoke')], max_length=1),
        ),
    ]
