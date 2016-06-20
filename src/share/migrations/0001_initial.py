# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LinkModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98', blank=True)),
                ('content', models.TextField(verbose_name=b'\xe9\x93\xbe\xe6\x8e\xa5', blank=True)),
                ('owner', models.CharField(max_length=100, verbose_name=b'owner', blank=True)),
            ],
        ),
    ]
