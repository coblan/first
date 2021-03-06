# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-19 14:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_srcmodel_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, verbose_name='\u540d\u79f0')),
                ('type', models.CharField(blank=True, choices=[(b'rst', b'rst'), (b'ck', b'ckEditor')], max_length=100, verbose_name='\u7c7b\u578b')),
                ('src', models.TextField(blank=True, verbose_name='\u6e90\u4ee3\u7801')),
                ('html', models.TextField(blank=True, verbose_name='html\u4ee3\u7801')),
                ('title', models.CharField(blank=True, max_length=300, verbose_name='\u6807\u9898')),
                ('statue', models.CharField(blank=True, choices=[(b'publish', b'publish'), (b'draft', b'draft')], max_length=100, verbose_name='\u72b6\u6001')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65e5\u671f')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CatModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, unique=True, verbose_name='name')),
                ('label', models.CharField(blank=True, max_length=100, verbose_name='\u663e\u793a\u540d\u5b57')),
            ],
        ),
        migrations.RemoveField(
            model_name='htmlart',
            name='src',
        ),
        migrations.RemoveField(
            model_name='htmlart',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='srcmodel',
            name='tag',
        ),
        migrations.DeleteModel(
            name='HtmlArt',
        ),
        migrations.DeleteModel(
            name='SrcModel',
        ),
        migrations.AddField(
            model_name='articlemodel',
            name='category',
            field=models.ForeignKey(blank=True, max_length=100, on_delete=django.db.models.deletion.CASCADE, to='blog.CatModel', verbose_name='\u5206\u7c7b'),
        ),
        migrations.AddField(
            model_name='articlemodel',
            name='tag',
            field=models.ManyToManyField(blank=True, to='blog.Tag'),
        ),
        migrations.AddField(
            model_name='tag',
            name='category',
            field=models.ManyToManyField(blank=True, to='blog.CatModel'),
        ),
    ]
