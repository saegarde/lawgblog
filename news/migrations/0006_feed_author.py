# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_article_domain'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='author',
            field=models.CharField(default='Pete Rivellini', max_length=200),
            preserve_default=False,
        ),
    ]
