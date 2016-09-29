# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0002_auto_20151220_0025'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dirmodel',
            name='chdir',
        ),
        migrations.AddField(
            model_name='dirmodel',
            name='p_dir',
            field=models.CharField(max_length=600, verbose_name=b'\xe7\x88\xb6\xe6\x96\x87\xe4\xbb\xb6\xe5\xa4\xb9', blank=True),
        ),
        migrations.AddField(
            model_name='notemodel',
            name='p_dir',
            field=models.CharField(max_length=100, verbose_name=b'\xe7\x88\xb6\xe6\x96\x87\xe4\xbb\xb6\xe5\xa4\xb9', blank=True),
        ),
    ]
