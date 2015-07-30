# -*- coding: utf-8 -*-
__author__ = 'artem'

from django.contrib import admin
from student.models import Student, Group, Log


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


class LogAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'log', 'model')
    search_fields = ('log',)
    list_filter = ('created_at',)


admin.site.register(Student, StudentAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Log, LogAdmin)