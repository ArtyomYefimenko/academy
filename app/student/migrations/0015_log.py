# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0014_delete_log'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('log', models.CharField(max_length=255, verbose_name='\u041e\u043f\u0435\u0440\u0430\u0446\u0438\u044f')),
                ('model', models.CharField(max_length=125, null=True, verbose_name='\u041e\u0431\u044a\u0435\u043a\u0442', blank=True)),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u0438')),
            ],
            options={
                'ordering': ['-created_at'],
                'verbose_name_plural': '\u0421\u0438\u0433\u043d\u0430\u043b\u044b',
            },
        ),
    ]
