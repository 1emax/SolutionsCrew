# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-14 10:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20170514_0921'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='level',
            field=models.PositiveIntegerField(default=0),
        ),
    ]