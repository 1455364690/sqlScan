# _*_coding:utf-8 _*_
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django_web.service import task_service
from django_web.service import user_service
from django_web.service import task_service


@login_required(login_url='/')
def get_report(request, task_id):
    data = {}
    menu = ['编号', '出错表格', '提测用户', '检测文件', '错误类型', '预警等级', '检测时间', '其他']
    # curr_user = user_service.get_user_by_id('1')[0]
    errors = task_service.get_error(task_id)
    curr_task = task_service.get_task_by_task_id(task_id)[0]
    curr_task_name = curr_task['file_name'][21:]
    error_list = []
    info = {}
    info['file_name'] = curr_task['file_name'][21:]
    info['user_name'] = request.user
    info['time'] = curr_task['create_time']
    info['last_time'] = '小于5分钟'
    data['menu'] = menu
    i = 1
    for error in errors:
        tmp = {}
        tmp['id'] = i
        tmp['table_name'] = error['mistake_detail']
        tmp['user_name'] = request.user
        tmp['file_name'] = curr_task_name
        tmp['mistake_type'] = error['mistake_type']
        tmp['mistake_grade'] = error['mistake_grade']
        tmp['time'] = error['find_time']
        tmp['other'] = '无'
        error_list.append(tmp)
        i += 1
    data['list'] = error_list
    data['info'] = info

    return render(request, 'report.html', data)
