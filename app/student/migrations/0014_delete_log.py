# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0013_auto_20150730_1924'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Log',
        ),
    ]
