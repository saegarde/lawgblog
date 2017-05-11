# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0014_feed_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='updated',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
