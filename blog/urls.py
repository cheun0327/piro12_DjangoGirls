from django.urls import path

from . import views

urlaptterns = [
    path('', views.post_list, name='post_list'),
]
