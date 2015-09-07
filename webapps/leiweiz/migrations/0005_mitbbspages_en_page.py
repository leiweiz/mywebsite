# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('leiweiz', '0004_remove_mitbbspages_en_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='mitbbspages',
            name='en_page',
            field=models.CharField(default=datetime.date(2015, 9, 7), max_length=50),
            preserve_default=False,
        ),
    ]
