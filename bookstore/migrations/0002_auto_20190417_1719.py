# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-17 15:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='content',
        ),
        migrations.RemoveField(
            model_name='book',
            name='design',
        ),
        migrations.RemoveField(
            model_name='book',
            name='usability',
        ),
        migrations.RemoveField(
            model_name='book',
            name='vote_submissions',
        ),
        migrations.AddField(
            model_name='book',
            name='book_category',
            field=models.CharField(max_length=40, null=True),
        ),
    ]