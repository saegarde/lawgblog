# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_auto_20170429_0241'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='practiceAreaSlug',
            field=models.CharField(default='Estate_Planning', max_length=30),
            preserve_default=False,
        ),
    ]
