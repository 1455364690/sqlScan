# -*- coding: UTF-8 -*-
import json
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django_web.models import *
from django_web.service.md5_service import md5
from django_web.service.check_login_service import *
from django.contrib.auth import login
from django_web.service import file_service
from django_web.service import task_service
import datetime


# Create your views here.



def test(request):
    return render(request, 'main.html')


def reg(request):
    if request.method == "POST":
        body = json.loads(request.body)
        username = body.get('username')
        password = body.get('password')
        password = md5(password)
        now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        temp = user(name=username, password=password, create_time=now_time, modify_time=now_time)
        temp.save()
        # save_user(username, password)
    temp = []
    # for i in show_user():
    #     temp.append({"user": i.name, "pwd": i.password})
    return render(request, 'index.html', {"data": temp})


def index(request):
    return render(request, 'index.html')


def get_list(request):
    return render(request, 'list.html')


