# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-21 16:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brewery', '0005_auto_20180221_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='slug',
            field=models.SlugField(blank=True, max_length=300),
        ),
    ]
