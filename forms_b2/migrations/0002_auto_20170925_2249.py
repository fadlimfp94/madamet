# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-09-25 15:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms_b2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='b2currentsmookinghabits',
            name='b4f_smoking_inside_house',
            field=models.CharField(blank=True, choices=[('', ''), ('1', 'Daily'), ('2', 'Weekly'), ('3', 'Monthly'), ('0', 'Never')], default='', max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='b2currentsmookinghabits',
            name='b4f_smoking_status',
            field=models.CharField(blank=True, choices=[('', ''), ('1', 'Smoker'), ('2', 'Ex-smoker'), ('0', 'Never smoke')], default='', max_length=1),
        ),
        migrations.AlterField(
            model_name='b2gestationalnutrition',
            name='b6m_alcohol',
            field=models.CharField(blank=True, choices=[('', ''), ('1', 'Daily'), ('2', 'Weekly'), ('3', 'Monthly'), ('0', 'Never')], default='', max_length=1),
        ),
        migrations.AlterField(
            model_name='b2gestationalnutrition',
            name='b6m_coffee',
            field=models.CharField(blank=True, choices=[('', ''), ('1', 'Daily'), ('2', 'Weekly'), ('3', 'Monthly'), ('0', 'Never')], default='', max_length=1),
        ),
        migrations.AlterField(
            model_name='b2gestationalnutrition',
            name='b6m_tea',
            field=models.CharField(blank=True, choices=[('', ''), ('1', 'Daily'), ('2', 'Weekly'), ('3', 'Monthly'), ('0', 'Never')], default='', max_length=1),
        ),
        migrations.AlterField(
            model_name='b2laboratorytest',
            name='b3m_cmv',
            field=models.CharField(blank=True, choices=[('', ''), ('1', 'Ig G'), ('2', 'Ig M'), ('0', 'No')], default='', max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='b2laboratorytest',
            name='b3m_herpes',
            field=models.CharField(blank=True, choices=[('', ''), ('1', 'Ig G'), ('2', 'Ig M'), ('0', 'No')], default='', max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='b2laboratorytest',
            name='b3m_proteinuria',
            field=models.CharField(choices=[('', ''), ('1', 'positif+'), ('2', 'positif++'), ('3', 'positif+++'), ('0', 'negative')], default='', max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='b2laboratorytest',
            name='b3m_rubella',
            field=models.CharField(choices=[('', ''), ('1', 'Ig G'), ('2', 'Ig M'), ('0', 'No')], default='', max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='b2laboratorytest',
            name='b3m_toxo',
            field=models.CharField(blank=True, choices=[('', ''), ('1', 'Ig G'), ('2', 'Ig M'), ('0', 'No')], default='', max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='b2pollutanexposure',
            name='b5m_garbage_burning',
            field=models.CharField(blank=True, choices=[('', ''), ('0', 'No'), ('1', 'Once per week or less'), ('2', 'More than once per week but not daily'), ('3', 'Daily')], default='', max_length=1),
        ),
    ]
