# -*- coding: utf-8 -*-
__author__ = 'artem'

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from student.models import Group, Student
from pure_pagination import PaginationMixin
from app.form import GroupAddForm, StudentAddForm


class GroupView(ListView):
    model = Group
    context_object_name = 'groups'
    template_name = "groups.html"



class GroupDetailView(PaginationMixin, ListView):
    model = Student
    object = Student
    paginate_by = 2
    template_name = "groups_detail.html"

    def get_queryset(self):
        return self.model.objects.filter(in_group__id=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super(GroupDetailView, self).get_context_data(**kwargs)
        context['group'] = Group.objects.get(id=self.kwargs['pk'])
        return context


class StudentDetailView(DetailView):
    model = Student
    template_name = 'student_detail.html'

    #def get_context_data(self, **kwargs):
     #   context = super(StudentDetailView, self).get_context_data(**kwargs)
      #  context['group'] = Group.objects.get(id=self.kwargs['pk'])
       # return context


class GroupAddView(CreateView):
    template_name = 'add_group.html'
    model = Group
    form_class = GroupAddForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super(GroupAddView, self).form_valid(form)

    def get_absolute_url(self):
        return '/group_detail/%s/' % (self.pk)


class StudentAddView(CreateView):
    template_name = 'add_student.html'
    model = Student
    form_class = StudentAddForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super(StudentAddView, self).form_valid(form)

    def get_absolute_url(self):
        return '/student_detail/%s/' % (self.pk)


class GroupEditView(UpdateView):
    template_name = 'edit_group.html'
    model = Group
    form_class = GroupAddForm

    def get_absolute_url(self):
        return '/group_detail/%s/' % (self.pk)


class StudentEditView(UpdateView):
    template_name = 'edit_student.html'
    model = Student
    form_class = StudentAddForm

    def get_absolute_url(self):
        return '/student_detail/%s/' % (self.pk)