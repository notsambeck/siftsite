# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-30 21:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labeller', '0003_auto_20170830_0150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='filename',
            field=models.FileField(upload_to='images', verbose_name='file path'),
        ),
    ]