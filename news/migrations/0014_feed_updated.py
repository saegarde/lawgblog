# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0013_auto_20170502_0312'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='updated',
            field=models.DateField(default=datetime.datetime(2017, 5, 6, 1, 33, 13, 451430, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
