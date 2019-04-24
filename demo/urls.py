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
from django.urls import re_path
from django.views.generic import TemplateView
from django_web.controller import task_controller
from django_web.controller import user_controller
from django_web.controller import file_controller
from django_web.controller import report_controller
from django_web import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('admin/', user_controller.admin_user),
    path('index/', views.index),
    path('', views.index),
    path('login/', user_controller.user_login),
    path('logout/', user_controller.user_logout),
    path('reactUser/', user_controller.react_user),
    path('freezeUser/', user_controller.freeze_user),
    path('test/', views.test),
    path('list/', task_controller.get_task),
    path('regView/', views.regView),
    path('reg/', user_controller.user_reg),
    path('upload/', file_controller.upload_file),
    path('startScan/', task_controller.start_task),
    re_path('^report/(\d+)/', report_controller.get_report),
    re_path('^reportDetail/(\d+)/', report_controller.report_detail),
]
