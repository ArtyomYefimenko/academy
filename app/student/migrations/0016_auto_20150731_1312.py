# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0015_log'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='photo',
            field=models.ImageField(upload_to=b'student_photo', null=True, verbose_name='\u0424\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u044f', blank=True),
        ),
    ]
