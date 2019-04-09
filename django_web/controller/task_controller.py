# _*_ coding:utf-8 _*_
from django.shortcuts import render
from django_web.service import task_service
from django_web.service import file_service
from django_web.service import collaborative_filtering_service
import json
from django.http import HttpResponse


def get_task(request):
    task_list = task_service.get_task_by_user_id('1')
    for task in task_list:
        task.file_name = task.file_name[21:]
    menu = ['编号', '文件名', '检测时间', '状态', '操作']
    data = {'menu': menu, 'task_list': task_list}
    return render(request, 'list.html', data)


def start_task(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        # task的id
        id = body.get('id')
        # 获取指定的task
        temp_task = task_service.get_task_by_task_id(id)[0]
        # 读取文件
        file_map = file_service.read_file(temp_task['file_name'])
        # 提取文件中所有的表名 list
        tables = file_service.get_tables(file_map['data'])
        package = {'name': temp_task['file_name'], 'tables': tables}
        # 协同过滤
        errors = collaborative_filtering_service.start(package)
        res = {'code': 0, 'message': '运行成功', 'data': errors}
        return HttpResponse(json.dumps(res))
