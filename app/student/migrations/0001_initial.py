# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
            ],
            options={
                'ordering': ['title'],
                'verbose_name': '\u0413\u0440\u0443\u043f\u043f\u0430',
                'verbose_name_plural': '\u0413\u0440\u0443\u043f\u043f\u044b',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_name', models.CharField(max_length=255, verbose_name='\u0424\u0430\u043c\u0438\u043b\u0438\u044f')),
                ('first_name', models.CharField(max_length=255, verbose_name='\u0418\u043c\u044f')),
                ('patronymic', models.CharField(max_length=255, verbose_name='\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e')),
                ('photo', models.ImageField(upload_to=b'student_photo', verbose_name='\u0424\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u044f')),
                ('birth_day', models.DateField(verbose_name='\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f')),
                ('students_ticket_number', models.PositiveIntegerField(verbose_name='\u041d\u043e\u043c\u0435\u0440 \u0441\u0442\u0443\u0434. \u0431\u0438\u043b\u0435\u0442\u0430')),
                ('in_group', models.ForeignKey(to='student.Group')),
            ],
            options={
                'ordering': ['last_name'],
                'verbose_name': '\u0421\u0442\u0443\u0434\u0435\u043d\u0442',
                'verbose_name_plural': '\u0421\u0442\u0443\u0434\u0435\u043d\u0442\u044b',
            },
        ),
        migrations.AddField(
            model_name='group',
            name='steward',
            field=models.ForeignKey(to='student.Student'),
        ),
    ]
