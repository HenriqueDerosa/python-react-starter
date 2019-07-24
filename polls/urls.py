from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('', views.index),
    path('test/', views.test),
]

urlpatterns += staticfiles_urlpatterns()