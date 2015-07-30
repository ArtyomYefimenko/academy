# -*- coding: utf-8 -*-
__author__ = 'artem'


from django.conf import settings


def context_settings(request):
    return {'settings': settings}