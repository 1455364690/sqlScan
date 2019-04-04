# -*- coding: UTF-8 -*-
import json

from django.shortcuts import render
from django_web.service.test_service import *


# Create your views here.


def index(request):
    if request.method == "POST":
        body = json.loads(request.body)
        username = request.POST.get('username')
        password = request.POST.get('password')
        save_user(username, password)
    temp = []
    for i in show_user():
        temp.append({"user": i.name, "pwd": i.password})
    return render(request, 'index.html', {"data": temp})


