# -*- coding: utf-8 -*-
__author__ = 'artem'

from django import forms
from student.models import Group, Student


class GroupAddForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ('title', 'steward')
        widgets = {
            'title': forms.TextInput(attrs={'class': "form-control"}),
        }


class StudentAddForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'last_name': forms.TextInput(attrs={'class': "form-control"}),
            'first_name': forms.TextInput(attrs={'class': "form-control"}),
            'patronymic': forms.TextInput(attrs={'class': "form-control"}),

        }