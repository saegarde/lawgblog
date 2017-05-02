# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_article_practiceareaslug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='practiceArea',
            field=models.CharField(max_length=30, choices=[(b'Trusts and Estates', b'Trusts and Estates'), (b'Criminal Law', b'Criminal Law'), (b'Real Estate Law', b'Real Estate Law'), (b'Tax Law', b'Tax Law'), (b'Family Law', b'Family Law'), (b'Personal Injury Law', b'Personal Injury Law'), (b'Litigation', b'Litigation')]),
        ),
    ]
