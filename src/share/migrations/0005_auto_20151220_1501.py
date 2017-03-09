# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0004_auto_20151220_1152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notemodel',
            name='meta',
        ),
        migrations.AlterField(
            model_name='notemodel',
            name='p_dir',
            field=models.ForeignKey(verbose_name=b'\xe7\x88\xb6\xe6\x96\x87\xe4\xbb\xb6\xe5\xa4\xb9', blank=True, to='share.DirModel', null=True),
        ),
    ]
