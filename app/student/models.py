# -*- coding: utf-8 -*-
__author__ = 'artem'


from django.db import models
from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.dispatch import receiver


class Student(models.Model):
    last_name = models.CharField(max_length=255, verbose_name=u'Фамилия')
    first_name = models.CharField(max_length=255, verbose_name=u'Имя')
    patronymic = models.CharField(max_length=255, verbose_name=u'Отчество')
    photo = models.ImageField(upload_to='student_photo',null=True, blank=True, verbose_name=u'Фотография')
    birth_day = models.DateField(auto_now=False, verbose_name=u'Дата рождения')
    students_ticket_number = models.PositiveIntegerField(verbose_name=u'Номер студ. билета')
    in_group = models.ForeignKey('Group', related_name='r_students', verbose_name=u'Группа')

    def __unicode__(self):
        return u"%s %s %s (группа %s)" % (self.last_name, self.first_name, self.patronymic, self.in_group)

    def get_absolute_url(self):
        return '/student_detail/%s/' % (self.pk)

    def name(self):
        return "{} {} {}".format(self.last_name, self.first_name, self.patronymic)

    class Meta:
        ordering = ['last_name', 'first_name']
        verbose_name = u'Студент'
        verbose_name_plural = u'Студенты'


class Group(models.Model):
    title = models.CharField(max_length=255, verbose_name=u'Название')
    steward = models.ForeignKey('Student', related_name='r_groups', null=True, blank=True, verbose_name=u'Староста группы')

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return '/group_detail/%s/' % (self.pk)

    class Meta:
        ordering = ['title']
        verbose_name = u'Группа'
        verbose_name_plural = u'Группы'


class Log(models.Model):
    log = models.CharField(max_length=255, verbose_name=u'Операция')
    model = models.CharField(max_length=125, null=True, blank=True, verbose_name=u'Объект')
    created_at = models.DateTimeField(auto_now=True, verbose_name=u'Дата и время операции')

    def __unicode__(self):
        return "{} {} {}".format(str(self.created_at), self.log, self.model)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = u'Сигналы'


@receiver(pre_save, sender=Student)
@receiver(pre_save, sender=Group)
def stud_and_group_saver(sender, instance, **kwargs):
    saver = Log()
    saver.model = str(sender._meta.model_name)

    try:
        sender.objects.get(pk=instance.pk)
        saver.log = 'изменён'

    except sender.DoesNotExist:
        saver.log = 'создан'

    saver.log = 'Объект <<{}>> {}'.format(instance, saver.log)
    saver.save()


@receiver(pre_delete, sender=Student)
@receiver(pre_delete, sender=Group)
def stud_and_group_delete(sender, instance, **kwargs):
    deleter = Log()
    deleter.model = str(sender._meta.model_name)
    deleter.log = 'Объект <<{}>> удалён'.format(instance)
    deleter.save()
