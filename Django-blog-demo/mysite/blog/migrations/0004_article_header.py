# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-10 00:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='header',
            field=models.ImageField(default='static/img/default.png', upload_to='static/img/headers/', verbose_name='用户头像'),
        ),
    ]