# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_auto_20150724_1241'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['last_name', 'first_name'], 'verbose_name': '\u0421\u0442\u0443\u0434\u0435\u043d\u0442\u0430', 'verbose_name_plural': '\u0421\u0442\u0443\u0434\u0435\u043d\u0442\u044b'},
        ),
    ]
