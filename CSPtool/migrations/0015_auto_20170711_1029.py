# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-11 15:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CSPtool', '0014_auto_20170707_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='plaintext',
            field=models.CharField(max_length=20000, null=True),
        ),
    ]
