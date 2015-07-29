# -*- coding: utf-8 -*-
__author__ = 'artem'

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from student.models import Group, Student
from pure_pagination import PaginationMixin
from app.form import GroupAddForm, GroupEditForm, StudentAddForm, RegistrationForm
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User


class GroupView(ListView):
    model = Group
    context_object_name = 'groups'
    template_name = "groups.html"

    def get_context_data(self, **kwargs):
        context = super(GroupView, self).get_context_data(**kwargs)
        context['is_group'] = True
        return context


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


class GroupAddView(CreateView):
    template_name = 'add_group.html'
    model = Group
    form_class = GroupAddForm

    def get_context_data(self, **kwargs):
        context = super(GroupAddView, self).get_context_data(**kwargs)
        context['is_add_group'] = True
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(GroupAddView, self).dispatch(*args, **kwargs)

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

    def get_context_data(self, **kwargs):
        context = super(StudentAddView, self).get_context_data(**kwargs)
        context['is_add_student'] = True
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(StudentAddView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super(StudentAddView, self).form_valid(form)

    def get_absolute_url(self):
        return '/student_detail/%s/' % (self.pk)


class GroupEditView(UpdateView):
    template_name = 'edit_group.html'
    model = Group
    form_class = GroupEditForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(GroupEditView, self).dispatch(*args, **kwargs)

    def get_absolute_url(self):
        return '/group_detail/%s/' % (self.pk)


class StudentEditView(UpdateView):
    template_name = 'edit_student.html'
    model = Student
    form_class = StudentAddForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(StudentEditView, self).dispatch(*args, **kwargs)

    def get_absolute_url(self):
        return '/student_detail/%s/' % (self.pk)


class GroupDeleteView(DeleteView):
    model = Group
    template_name = 'delete_group.html'
    success_url = reverse_lazy('home')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(GroupDeleteView, self).dispatch(*args, **kwargs)


class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'delete_student.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(StudentDeleteView, self).dispatch(*args, **kwargs)

    def get_success_url(self):
        group_id = self.object.in_group.id
        return reverse('group_detail', args=(group_id,))


class RegistrationView(CreateView):
    template_name = 'registration/registration.html'
    model = User
    form_class = RegistrationForm
    success_url = reverse_lazy('login')