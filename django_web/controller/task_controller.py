# _*_ coding:utf-8 _*_
from django.shortcuts import render
from django_web.service import task_service
from django_web.service import file_service
from django_web.service import user_service
import json
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required


@login_required(login_url='/')
def get_task(request):
    user_id = user_service.get_user_by_name(request.user)[0]['id']
    task_list = task_service.get_task_by_user_id(user_id)
    for task in task_list:
        task.file_name = task.file_name[21:]
    menu = ['编号', '文件名', '检测时间', '状态', '操作']
    data = {'menu': menu, 'task_list': task_list}
    return render(request, 'list.html', data)


@login_required(login_url='/')
def start_task(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        # task的id
        # task_id = body.get('id')
        # # 执行任务，进行检测
        # task_run_state = task_service.start_task(task_id)
        # # 修改任务状态
        # if task_run_state['code'] == 0:
        #     task_service.task_success(task_id)
        # else:
        #     task_service.task_fail(task_id)
        task_service.test('ucr_iupc.PM_OFFER_REL', 'REL_OFFER_ID')
        return HttpResponse(json.dumps({}))
