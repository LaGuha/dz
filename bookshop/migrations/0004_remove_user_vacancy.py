# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-20 17:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookshop', '0003_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='vacancy',
        ),
    ]
