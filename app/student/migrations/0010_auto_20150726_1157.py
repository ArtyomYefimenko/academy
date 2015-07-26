# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0009_auto_20150726_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='steward',
            field=models.ForeignKey(related_name='r_groups', verbose_name='\u0421\u0442\u0430\u0440\u043e\u0441\u0442\u0430 \u0433\u0440\u0443\u043f\u043f\u044b', blank=True, to='student.Student', null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='in_group',
            field=models.ForeignKey(related_name='r_students', verbose_name='\u0413\u0440\u0443\u043f\u043f\u0430', to='student.Group'),
        ),
    ]
