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


from django.contrib.auth.decorators import login_required


@login_required(login_url='/')
def test(request):
    return render(request, 'main.html')


def regView(request):
    return render(request, 'reg.html')





def index(request):
    return render(request, 'index.html')


def get_list(request):
    return render(request, 'list.html')


