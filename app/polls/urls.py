#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian


from django.urls import path

from . import views
# app_name 设置命名空间
app_name = 'polls'

urlpatterns = [
    # 为你的 URL 取名能使你在 Django 的任意地方唯一地引用它，尤其是在模板中。
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),

    path('dashboard', views.dashboard, name='dashboard'),
]