# -*- coding: utf-8 -*-
__author__ = 'artem'

from django import forms
from student.models import Group, Student


class GroupAddForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ('title',  )
        widgets = {
            'title': forms.TextInput(attrs={'class': "form-control"}),
        }


class GroupEditForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ('title', 'steward')
        widgets = {
            'title': forms.TextInput(attrs={'class': "form-control"}),
            'steward': forms.Select(attrs={'class': "form-control"}),
        }


class StudentAddForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('last_name', 'first_name', 'patronymic', 'birth_day', 'students_ticket_number', 'in_group', 'photo')
        widgets = {
            'last_name': forms.TextInput(attrs={'class': "form-control"}),
            'first_name': forms.TextInput(attrs={'class': "form-control"}),
            'patronymic': forms.TextInput(attrs={'class': "form-control"}),
            'birth_day': forms.DateInput(attrs={'class': "form-control"}),
            'in_group': forms.Select(attrs={'class': "form-control"}),
            'students_ticket_number': forms.TextInput(attrs={'class': "form-control"}),

        }