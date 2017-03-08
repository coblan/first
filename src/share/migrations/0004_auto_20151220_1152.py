# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0003_auto_20151220_0037'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notemodel',
            name='title',
        ),
        migrations.AddField(
            model_name='notemodel',
            name='name',
            field=models.CharField(max_length=200, verbose_name=b'\xe5\x90\x8d\xe5\xad\x97', blank=True),
        ),
        migrations.AlterField(
            model_name='dirmodel',
            name='p_dir',
            field=models.ForeignKey(verbose_name=b'\xe7\x88\xb6\xe6\x96\x87\xe4\xbb\xb6\xe5\xa4\xb9', blank=True, to='share.DirModel', null=True),
        ),
        migrations.AlterField(
            model_name='notemodel',
            name='p_dir',
            field=models.ForeignKey(verbose_name=b'\xe7\x88\xb6\xe6\x96\x87\xe4\xbb\xb6\xe5\xa4\xb9', blank=True, to='share.DirModel'),
        ),
    ]
