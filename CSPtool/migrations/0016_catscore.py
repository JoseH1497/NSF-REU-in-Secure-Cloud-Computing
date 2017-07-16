# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-11 16:28
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CSPtool', '0015_auto_20170711_1029'),
    ]

    operations = [
        migrations.CreateModel(
            name='CatScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=12)),
                ('value', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)])),
                ('CSP', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CSPtool.CSP')),
            ],
        ),
    ]
