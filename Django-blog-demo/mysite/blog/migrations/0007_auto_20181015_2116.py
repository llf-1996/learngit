# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-15 13:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20181012_2145'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-publishTime'], 'verbose_name_plural': '文章'},
        ),
        migrations.AddField(
            model_name='article',
            name='remark',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='摘要'),
        ),
    ]