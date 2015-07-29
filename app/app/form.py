# -*- coding: utf-8 -*-
__author__ = 'artem'

from django import forms
from student.models import Group, Student
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


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


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(label='Email', max_length=75,
        widget=forms.EmailInput(attrs={'class': "form-control"}))
    password1 = forms.CharField(label=("Пароль"),
        widget=forms.PasswordInput(attrs={'class': "form-control"}))
    password2 = forms.CharField(label=("Пароль повторно"),
        widget=forms.PasswordInput(attrs={'class': "form-control"}),
        help_text=("Введите повторно пароль"))
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')
        widgets = {
            'username': forms.TextInput(attrs={'class': "form-control"}),
        }


    def clean_email(self):

        email = self.cleaned_data["email"]
        try:
            user = User.objects.get(email=email)
            raise forms.ValidationError("Этот адрес электронной почты уже занят")
        except User.DoesNotExist:
            return email

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data["email"]
        user.is_active = True
        if commit:
            user.save()
        return user