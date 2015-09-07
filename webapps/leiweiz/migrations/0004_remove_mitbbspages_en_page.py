# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leiweiz', '0003_auto_20150906_2355'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mitbbspages',
            name='en_page',
        ),
    ]
