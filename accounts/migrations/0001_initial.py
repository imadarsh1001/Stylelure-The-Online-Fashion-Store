# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-28 05:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('is_active', models.BooleanField(default=True)),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('phone_number', models.CharField(max_length=15)),
                ('street_address_1', models.CharField(blank=True, max_length=256)),
                ('street_address_2', models.CharField(blank=True, max_length=256)),
                ('city', models.CharField(blank=True, max_length=256)),
                ('state', models.CharField(blank=True, max_length=128)),
                ('postal_code', models.CharField(blank=True, max_length=20)),
                ('country', django_countries.fields.CountryField(max_length=2)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
