# _*_ coding:utf-8 _*_
"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.views.generic import TemplateView
from django_web.controller import task_controller
from django_web.controller import user_controller
from django_web.controller import file_controller
from django_web.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index),
    path('', index),
    path('login/', user_controller.user_login),
    path('test/', test),
    path('list/', task_controller.get_task),
    path('reg/', reg),
    path('upload/', file_controller.upload_file)
]
