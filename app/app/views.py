# -*- coding: utf-8 -*-
__author__ = 'artem'

from django.views.generic import ListView
from student.models import Group


class GroupView(ListView):
    model = Group
    context_object_name = 'groups'
    template_name = "groups.html"

