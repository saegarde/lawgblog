# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0011_auto_20170501_0133'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='authorSlug',
            field=models.CharField(default='none', max_length=200),
            preserve_default=False,
        ),
    ]
