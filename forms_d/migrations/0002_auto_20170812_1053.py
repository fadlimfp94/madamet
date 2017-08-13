# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-08-12 03:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms_d', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dinfant',
            name='child_id',
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.AlterField(
            model_name='dinfant',
            name='child_name',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='dinfant',
            name='data_check_id',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='dinfant',
            name='data_entry_id',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='dinfant',
            name='date_admission',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='dinfant',
            name='date_data_checked',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='dinfant',
            name='date_data_entered',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='dinfant',
            name='date_interviewed',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='dinfant',
            name='interviewer_id',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='dinfant2',
            name='child_id',
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.AlterField(
            model_name='dinfant2',
            name='child_name',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='dinfant2',
            name='data_check_id',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='dinfant2',
            name='data_entry_id',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='dinfant2',
            name='date_admission',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='dinfant2',
            name='date_data_checked',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='dinfant2',
            name='date_data_entered',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='dinfant2',
            name='date_interviewed',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='dinfant2',
            name='interviewer_id',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='dinfant3',
            name='child_id',
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.AlterField(
            model_name='dinfant3',
            name='child_name',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='dinfant3',
            name='data_check_id',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='dinfant3',
            name='data_entry_id',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='dinfant3',
            name='date_admission',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='dinfant3',
            name='date_data_checked',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='dinfant3',
            name='date_data_entered',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='dinfant3',
            name='date_interviewed',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='dinfant3',
            name='interviewer_id',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='dinfant4',
            name='child_id',
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.AlterField(
            model_name='dinfant4',
            name='child_name',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='dinfant4',
            name='data_check_id',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='dinfant4',
            name='data_entry_id',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='dinfant4',
            name='date_admission',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='dinfant4',
            name='date_data_checked',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='dinfant4',
            name='date_data_entered',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='dinfant4',
            name='date_interviewed',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='dinfant4',
            name='interviewer_id',
            field=models.CharField(blank=True, max_length=25),
        ),
    ]
