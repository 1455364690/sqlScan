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
import datetime


# Create your views here.


def user_login(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        username = body.get('username')
        password = body.get('password')
        res = check_login(username, password)
        return HttpResponse(json.dumps(res), content_type='application/json')


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


def upload_file_controller(request):
    files = request.FILES
    file = None
    if files:
        for i in files:
            file = files[i]
    data = {}
    if file:
        file_map = file_service.upload_file(file)
        data = file_map
    else:
        data['code'] = 2
        data['message'] = '文件上传失败'
    return HttpResponse(json.dumps(data))
