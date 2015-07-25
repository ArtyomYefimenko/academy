# -*- coding: utf-8 -*-
__author__ = 'artem'

from django.contrib import admin
from student.models import Student, Group


class StudentInline(admin.TabularInline):
    model = Student
    extra = 1


class GroupInline(admin.TabularInline):
    model = Group
    extra = 1


class StudentAdmin(admin.ModelAdmin):
    inlines = [
        GroupInline,
    ]


class GroupAdmin(admin.ModelAdmin):
    inlines = [
        StudentInline,
    ]


admin.site.register(Student, StudentAdmin)
admin.site.register(Group, GroupAdmin)