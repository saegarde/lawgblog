# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_auto_20170426_0323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='author',
            field=models.CharField(max_length=250, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='feed',
            name='practiceArea',
            field=models.CharField(max_length=100),
        ),
    ]
