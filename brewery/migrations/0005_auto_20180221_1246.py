# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-21 12:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brewery', '0004_auto_20180206_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='slug',
            field=models.SlugField(max_length=300),
        ),
    ]