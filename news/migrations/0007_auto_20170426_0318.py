# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_feed_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='author',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
