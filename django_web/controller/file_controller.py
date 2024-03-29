# _*_ coding:utf-8 _*_

import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from django_web.service import user_service
from django_web.service import file_service, task_service


@login_required(login_url='/')
def upload_file(request):
    files = request.FILES
    file = None
    if files:
        for i in files:
            file = files[i]
    data = {}
    if file:
        file_map = file_service.upload_file(file)
        data = file_map
        user_id = user_service.get_user_by_name(request.user)[0]['id']
        task_service.create_task(user_id, file_map['file_name'])
    else:
        data['code'] = 2
        data['message'] = '文件上传失败'
    return HttpResponse(json.dumps(data))

@login_required(login_url='/')
def read_file(request, task_id):
    tmp_task = task_service.get_task_by_task_id(task_id)[0]
    res = file_service.read_file(tmp_task['file_name'])
    return render(request, 'file.html', res)
