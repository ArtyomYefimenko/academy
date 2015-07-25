# -*- coding: utf-8 -*-
__author__ = 'artem'

from django.views.generic import ListView, DetailView
from student.models import Group, Student


class GroupView(ListView):
    model = Group
    context_object_name = 'groups'
    template_name = "groups.html"


class GroupDetailView(DetailView):
    model = Group
    template_name = "groups_detail.html"

    def get_context_data(self, **kwargs):
        context = super(GroupDetailView, self).get_context_data(**kwargs)
        context['students'] = Student.objects.all()
        return context

