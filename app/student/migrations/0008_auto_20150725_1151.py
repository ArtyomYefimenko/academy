# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_auto_20150724_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='in_group',
            field=models.ForeignKey(related_name='students', verbose_name='\u0413\u0440\u0443\u043f\u043f\u0430', to='student.Group'),
        ),
    ]
