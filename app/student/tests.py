# -*- coding: utf-8 -*-
__author__ = 'artem'


from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class StudentTestCase(TestCase):
    username = 'test'
    password = 'passw'
    password1 = 'passw'
    email = 'test@mail.com'
    group = {'title': 'group'}
    student = {
              'last_name': 'testname',
              'first_name': 'testname',
              'patronymic': 'test',
              'birth_date': '1991-03-27',
              'students_ticket_number': '999999',
              'in_group': 'group',
              }


    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(self)
        self.client.login()

    def test_login(self):
        response = self.client.post(reverse('login'), {'username': self.username,
                                                       'password': self.password})
        self.assertEqual(response.status_code, 200)

    def test_add_group_and_student_in_it(self):
        response = self.client.post(reverse('add_group'), self.group)
        self.assertEqual(response.status_code, 302)

        response = self.client.post(reverse('add_student'), self.student)
        self.assertEquals(response.status_code, 302)

        print u'\nТест выполнен успешно'