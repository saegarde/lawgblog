# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0015_auto_20170506_0203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='updated',
            field=models.DateField(default=datetime.datetime(2017, 5, 6, 2, 50, 20, 77563, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
