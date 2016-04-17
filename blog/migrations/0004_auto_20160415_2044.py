# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-15 12:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20160414_0002'),
    ]

    operations = [
        migrations.AddField(
            model_name='srcmodel',
            name='category',
            field=models.CharField(blank=True, choices=[(b'common', b'common'), (b'math', b'math')], max_length=100, verbose_name='\u5206\u7c7b'),
        ),
        migrations.AddField(
            model_name='srcmodel',
            name='title',
            field=models.CharField(blank=True, max_length=300, verbose_name='\u6807\u9898'),
        ),
    ]
