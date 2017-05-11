# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0016_auto_20170506_0250'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='modified',
            field=models.DateField(default=datetime.datetime(2017, 5, 6, 3, 59, 20, 927155, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
