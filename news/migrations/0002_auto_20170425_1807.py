# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PracticeArea',
        ),
        migrations.AddField(
            model_name='feed',
            name='practiceArea',
            field=models.CharField(default='Estate Planning', max_length=30),
            preserve_default=False,
        ),
    ]
