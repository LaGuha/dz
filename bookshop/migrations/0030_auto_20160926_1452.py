# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookshop', '0029_auto_20160926_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='img',
            field=models.ImageField(upload_to='bookshop/static/'),
        ),
    ]
