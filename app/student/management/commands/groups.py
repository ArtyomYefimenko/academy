# -*- coding: utf-8 -*-
__author__ = 'artem'

"""python manage.py groups auth"""

from django.core.management.base import AppCommand
from student.models import Student, Group


class Command(AppCommand):
    requires_system_checks = True

    def handle_app_config(self, app_config, **options):
        groups = Group.objects.all()
        groups_list = []

        for group in groups:
            groups_list.append(u'\t \t Группа "%s":\n' % group.title)
            i = 1

            for student in Student.objects.filter(in_group=group.id):
                groups_list.append("%s. %s %s %s\n" % (i, student.last_name, student.first_name, student.patronymic))
                i += 1

        return "\n".join(groups_list)
