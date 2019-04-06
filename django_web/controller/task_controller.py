# _*_ coding:utf-8 _*_
from django.shortcuts import render
from django_web.service import task_service
import json
from django.http import HttpResponse


def get_task(request):
    task_list = task_service.get_task_by_user_id('1')
    menu = ['编号', '文件名', '检测时间', '状态']
    data = {'menu': menu, 'task_list': task_list}
    return render(request, 'list.html', data)
