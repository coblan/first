# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-30 13:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20160425_2244'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='label',
            field=models.CharField(blank=True, max_length=100, verbose_name='\u6807\u7b7e'),
        ),
    ]