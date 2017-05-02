# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20170426_0227'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='domain',
            field=models.URLField(default='nus.com'),
            preserve_default=False,
        ),
    ]
