# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0020_auto_20170506_0417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='modified',
            field=models.CharField(max_length=200),
        ),
    ]
