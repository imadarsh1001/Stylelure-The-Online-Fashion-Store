# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-28 05:49
from __future__ import unicode_literals

import colorfield.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category_name', models.CharField(db_index=True, default='Other', max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Model_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Model_Category_name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'model_category',
                'verbose_name_plural': 'model_categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=30)),
                ('slug', models.SlugField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, default=39.99, max_digits=20)),
                ('discounted_price', models.DecimalField(decimal_places=2, default=39.99, max_digits=20)),
                ('short_description', models.TextField(blank=True)),
                ('description', models.TextField(blank=True)),
                ('featured', models.BooleanField(default=False)),
                ('new_collection', models.BooleanField(default=False)),
                ('stock', models.PositiveIntegerField(default=2)),
                ('Manufacturer', models.CharField(max_length=50)),
                ('Occassion', models.CharField(max_length=50)),
                ('Season', models.CharField(max_length=50)),
                ('Gender', models.CharField(max_length=50)),
                ('available_size', models.CharField(max_length=50)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('sku', models.CharField(max_length=32, unique=True)),
                ('category', models.ForeignKey(default='Other', on_delete=django.db.models.deletion.CASCADE, related_name='products', to='Products.Category')),
                ('model_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='model_products', to='Products.Model_Category')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='ProductColors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available_color', colorfield.fields.ColorField(max_length=18)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='colors', to='Products.Product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='products/%Y/%m/%d')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='Products.Product')),
            ],
        ),
        migrations.AlterIndexTogether(
            name='product',
            index_together=set([('id', 'slug')]),
        ),
    ]
