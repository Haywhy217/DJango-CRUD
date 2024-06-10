from django.urls import path
from django.shortcuts import render
from.views import getusers,add_users,edit_users,delete_users


urlpatterns = [
  path('getusers/', getusers, name="getusers"),
  path('add_users/', add_users, name="add_users"),
  path('edit_users/', edit_users, name="edit_users"),
  path('delete_users/', delete_users, name="delete_users")
]