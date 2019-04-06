# _*_ coding:utf-8 _*_

import json

from django.http import HttpResponse

from django_web.service import file_service, task_service


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
        print(task_service.create_task('1', file_map['file_name']))
    else:
        data['code'] = 2
        data['message'] = '文件上传失败'
    return HttpResponse(json.dumps(data))
