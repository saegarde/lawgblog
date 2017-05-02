# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_auto_20170426_0318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='author',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
