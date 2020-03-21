# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 22:46:16 2020

@author: Lenovo
"""

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^user/create/$', views.UserCreateView.as_view(), name="user_create"),
    url(r'^users/list/$', views.UsersListView.as_view(), name="users_list"),
    url(r'^users/(?P<pk>\d+)/detail/$', views.UserDetailView.as_view(), name="user_detail"),
    url(r'^users/(?P<pk>\d+)/update/$', views.UserUpdateView.as_view(), name="user_update"),
    url(r'^users/(?P<pk>\d+)/delete/$', views.UserDeleteView.as_view(), name="user_delete"),    
]