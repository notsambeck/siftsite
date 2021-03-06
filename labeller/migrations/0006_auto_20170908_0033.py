# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-08 00:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labeller', '0005_auto_20170907_0612'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='net',
            field=models.CharField(max_length=512, null=True, verbose_name="neural network that id'd image"),
        ),
        migrations.AddField(
            model_name='image',
            name='probability',
            field=models.FloatField(null=True, verbose_name='sift-generated probability that is image'),
        ),
    ]
