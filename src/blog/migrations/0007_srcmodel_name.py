# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-15 13:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20160415_2105'),
    ]

    operations = [
        migrations.AddField(
            model_name='srcmodel',
            name='name',
            field=models.CharField(blank=True, max_length=100, verbose_name='\u540d\u79f0'),
        ),
    ]
