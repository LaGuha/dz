# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookshop', '0006_book_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='img',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='book',
            name='number',
            field=models.IntegerField(),
        ),
    ]
