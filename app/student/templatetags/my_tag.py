# -*- coding: utf-8 -*-
__author__ = 'artem'


from django import template
from django.core.urlresolvers import reverse


register = template.Library()


@register.simple_tag
def in_admin(object, title):
    url1 = '<a href="/admin/%s/%s/%s/"><button type="button" class="btn btn-warning">' % (object._meta.app_label, object._meta.model_name, object.pk)
    url2 = u'%s' % (title)
    url3 = '</button></a>'
    return url1 + url2 + url3