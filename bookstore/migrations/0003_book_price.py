# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-17 15:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0002_auto_20190417_1719'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
