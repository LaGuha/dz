# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookshop', '0012_auto_20160921_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='img',
            field=models.ImageField(upload_to='bookshop/static'),
        ),
    ]
