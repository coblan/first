# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-24 13:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagebuilder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MobilePage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=300, verbose_name='name')),
                ('label', models.CharField(blank=True, max_length=400, verbose_name='label')),
                ('content', models.TextField(blank=True, verbose_name='content')),
            ],
        ),
    ]
