# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-01-15 21:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserProfile', '0003_auto_20190115_2106'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='name',
            field=models.CharField(default='default', max_length=30),
            preserve_default=False,
        ),
    ]