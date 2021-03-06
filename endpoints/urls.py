"""ATBC02P01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hello', views.hello, name='hello'),
    path('hello_name/<name>', views.hello_name, name='hello_name'),
    path('index', views.project_index, name="project_index"),
    path('new/', views.project_new, name='project_new'),
    path('index/<int:pk>/', views.edit, name="project_edit"),
    path('delete/<int:pk>/', views.delete, name="project_delete"),
    path('solve/<int:pk>/', views.project_solve, name="project_solve"),
    path('run/', views.project_run, name="project_run"),
]

