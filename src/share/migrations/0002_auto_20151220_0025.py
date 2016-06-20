# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DirModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'\xe5\x90\x8d\xe5\xad\x97', blank=True)),
                ('chdir', models.CharField(max_length=600, verbose_name=b'\xe5\xad\x90\xe6\x96\x87\xe4\xbb\xb6', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='NoteModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98', blank=True)),
                ('content', models.TextField(verbose_name=b'\xe5\x86\x85\xe5\xae\xb9', blank=True)),
                ('meta', models.CharField(max_length=200, verbose_name=b'meta', blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='LinkModel',
        ),
    ]
