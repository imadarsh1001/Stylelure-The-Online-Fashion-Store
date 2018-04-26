# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-26 05:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0012_auto_20180425_1729'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='new_collection',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.CharField(max_length=32, unique=True),
        ),
    ]