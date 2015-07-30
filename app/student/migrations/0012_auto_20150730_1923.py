# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0011_log'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='log',
            options={'ordering': ['-created_at'], 'verbose_name_plural': '\u0421\u0438\u0433\u043d\u0430\u043b\u044b'},
        ),
        migrations.AlterField(
            model_name='log',
            name='log',
            field=models.CharField(max_length=125, verbose_name='\u0421\u0442\u0443\u0434\u0435\u043d\u0442'),
        ),
        migrations.AlterField(
            model_name='log',
            name='model',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
