# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-09-26 15:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forms_d', '0010_auto_20170924_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='d1infantgrowth2',
            name='d_form',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='forms_d.DInfant2'),
        ),
        migrations.AlterField(
            model_name='d1infantgrowth3',
            name='d_form',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='forms_d.DInfant3'),
        ),
        migrations.AlterField(
            model_name='d1infantgrowth4',
            name='d_form',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='forms_d.DInfant4'),
        ),
        migrations.AlterField(
            model_name='d2infantfeeding2',
            name='d_form',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='forms_d.DInfant2'),
        ),
        migrations.AlterField(
            model_name='d2infantfeeding3',
            name='d_form',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='forms_d.DInfant3'),
        ),
        migrations.AlterField(
            model_name='d2infantfeeding4',
            name='d_form',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='forms_d.DInfant4'),
        ),
        migrations.AlterField(
            model_name='d3infantcardiovascular2',
            name='d_form',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='forms_d.DInfant2'),
        ),
        migrations.AlterField(
            model_name='d3infantcardiovascular3',
            name='d_form',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='forms_d.DInfant3'),
        ),
        migrations.AlterField(
            model_name='d3infantcardiovascular4',
            name='d_form',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='forms_d.DInfant4'),
        ),
        migrations.AlterField(
            model_name='d4infantlungfunction2',
            name='d_form',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='forms_d.DInfant2'),
        ),
        migrations.AlterField(
            model_name='d4infantlungfunction3',
            name='d_form',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='forms_d.DInfant3'),
        ),
        migrations.AlterField(
            model_name='d4infantlungfunction4',
            name='d_form',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='forms_d.DInfant4'),
        ),
        migrations.AlterField(
            model_name='d5infantbiological2',
            name='d_form',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='forms_d.DInfant2'),
        ),
        migrations.AlterField(
            model_name='d5infantbiological3',
            name='d_form',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='forms_d.DInfant3'),
        ),
        migrations.AlterField(
            model_name='d5infantbiological4',
            name='d_form',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='forms_d.DInfant4'),
        ),
        migrations.AlterField(
            model_name='d6currentsmoking2',
            name='d_form',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='forms_d.DInfant2'),
        ),
        migrations.AlterField(
            model_name='d6currentsmoking3',
            name='d_form',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='forms_d.DInfant3'),
        ),
        migrations.AlterField(
            model_name='d6currentsmoking4',
            name='d_form',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='forms_d.DInfant4'),
        ),
        migrations.AlterField(
            model_name='d7infection2',
            name='d_form',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='forms_d.DInfant2'),
        ),
        migrations.AlterField(
            model_name='d7infection3',
            name='d_form',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='forms_d.DInfant3'),
        ),
        migrations.AlterField(
            model_name='d7infection4',
            name='d_form',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='forms_d.DInfant4'),
        ),
        migrations.AlterField(
            model_name='d8pollutantexposure2',
            name='d_form',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='forms_d.DInfant2'),
        ),
        migrations.AlterField(
            model_name='d8pollutantexposure3',
            name='d_form',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='forms_d.DInfant3'),
        ),
        migrations.AlterField(
            model_name='d8pollutantexposure4',
            name='d_form',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='forms_d.DInfant4'),
        ),
    ]
