# -*- coding: utf-8 -*-
__author__ = 'artem'

from django.views.generic import ListView, DetailView
from student.models import Group, Student
from pure_pagination import PaginationMixin



class GroupView(ListView):
    model = Group
    context_object_name = 'groups'
    template_name = "groups.html"

class GroupDetailView(PaginationMixin, DetailView):
    model = Group
    object = Group
    paginate_by = 2
    template_name = "groups_detail.html"
    #context_object_name = 'counter'