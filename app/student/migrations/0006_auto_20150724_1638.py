# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_auto_20150724_1637'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'ordering': ['title'], 'verbose_name': '\u0413\u0440\u0443\u043f\u043f\u0443', 'verbose_name_plural': '\u0413\u0440\u0443\u043f\u043f\u044b'},
        ),
    ]
