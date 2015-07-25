# -*- coding: utf-8 -*-
__author__ = 'artem'


from django.db import models


class Student(models.Model):
    last_name = models.CharField(max_length=255, verbose_name=u'Фамилия')
    first_name = models.CharField(max_length=255, verbose_name=u'Имя')
    patronymic = models.CharField(max_length=255, verbose_name=u'Отчество')
    photo = models.ImageField(upload_to='student_photo', verbose_name=u'Фотография')
    birth_day = models.DateField(auto_now=False, verbose_name=u'Дата рождения')
    students_ticket_number = models.PositiveIntegerField(verbose_name=u'Номер студ. билета')
    in_group = models.ForeignKey('Group', related_name='students', verbose_name=u'Группа')

    def __unicode__(self):
        return u"%s %s %s" % (self.last_name, self.first_name, self.patronymic)

    class Meta:
        ordering = ['last_name', 'first_name']
        verbose_name = u'Студент'
        verbose_name_plural = u'Студенты'


class Group(models.Model):
    title = models.CharField(max_length=255, verbose_name=u'Название')
    steward = models.ForeignKey('Student', null=True, blank=True, verbose_name=u'Староста группы')

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = u'Группа'
        verbose_name_plural = u'Группы'