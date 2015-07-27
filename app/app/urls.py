"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from app.views import GroupView, GroupDetailView, StudentDetailView, GroupAddView, StudentAddView, GroupEditView, StudentEditView
from settings import DEBUG, MEDIA_ROOT



urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', GroupView.as_view(), name='home'),
    url(r'^group_detail/(?P<pk>\d+)/$', GroupDetailView.as_view(), name='group_detail'),
    url(r'^student_detail/(?P<pk>\d+)/$', StudentDetailView.as_view(), name='student_detail'),

    url(r'^add_group', GroupAddView.as_view(), name='add_group'),
    url(r'^add_student', StudentAddView.as_view(), name='add_student'),

    url(r'^edit_group/(?P<pk>\d+)/$', GroupEditView.as_view(), name='edit_group'),
    url(r'^edit_student/(?P<pk>\d+)/$', StudentEditView.as_view(), name='edit_student'),

)


if DEBUG:
    urlpatterns += patterns('',
                            (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                                'document_root': MEDIA_ROOT}))