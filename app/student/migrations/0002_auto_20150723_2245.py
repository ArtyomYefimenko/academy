# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='steward',
            field=models.ForeignKey(verbose_name='\u0421\u0442\u0430\u0440\u043e\u0441\u0442\u0430 \u0433\u0440\u0443\u043f\u043f\u044b', to='student.Student'),
        ),
        migrations.AlterField(
            model_name='student',
            name='in_group',
            field=models.ForeignKey(verbose_name='\u0413\u0440\u0443\u043f\u043f\u0430', to='student.Group'),
        ),
    ]
