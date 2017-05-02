# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20170425_1807'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='practiceArea',
            field=models.CharField(default='Criminal Law', max_length=30),
            preserve_default=False,
        ),
    ]
