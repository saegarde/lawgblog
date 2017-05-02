# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0012_article_authorslug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='url',
            field=models.URLField(unique=True),
        ),
    ]
