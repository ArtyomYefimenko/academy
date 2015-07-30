# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0012_auto_20150730_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='log',
            field=models.CharField(max_length=255, verbose_name='\u0421\u0442\u0443\u0434\u0435\u043d\u0442'),
        ),
        migrations.AlterField(
            model_name='log',
            name='model',
            field=models.CharField(max_length=125, null=True, blank=True),
        ),
    ]
