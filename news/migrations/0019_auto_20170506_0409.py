# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0018_auto_20170506_0403'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feed',
            name='updated',
        ),
        migrations.AddField(
            model_name='feed',
            name='etag',
            field=models.CharField(default=datetime.datetime(2017, 5, 6, 4, 9, 37, 735076, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='feed',
            name='modified',
            field=models.DateField(),
        ),
    ]
