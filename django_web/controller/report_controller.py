# _*_coding:utf-8 _*_
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django_web.service import task_service
from django_web.service import user_service
from django_web.service import mistake_service
from django_web.service import task_service


@login_required(login_url='/')
def get_report(request, task_id):
    data = {}
    menu = ['编号', '错误详情', '提测用户', '检测文件', '错误类型', '预警等级', '检测时间', '其他']
    # curr_user = user_service.get_user_by_id('1')[0]
    table_errors = task_service.get_table_error(task_id)
    attribute_errors = task_service.get_attribute_error(task_id)
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
    # 数据库表错误
    table_errors_dict = {}
    attribute_errors_dict = {}
    for error in table_errors:
        table_errors_dict[error['mistake_grade']] = table_errors_dict.get(error['mistake_grade'], 0) + 1
        tmp = {}
        tmp['number'] = i
        tmp['id'] = error['id']
        tmp['mistake_detail'] = error['mistake_detail']
        tmp['user_name'] = request.user
        tmp['file_name'] = curr_task_name
        tmp['mistake_type'] = error['mistake_type']
        tmp['mistake_grade'] = error['mistake_grade']
        tmp['time'] = error['find_time']
        tmp['other'] = '无'
        error_list.append(tmp)
        i += 1
    # 关键属性错误
    for error in attribute_errors:
        attribute_errors_dict[error['mistake_grade']] = attribute_errors_dict.get(error['mistake_grade'], 0) + 1
        tmp = {}
        tmp['number'] = i
        tmp['id'] = error['id']
        tmp['mistake_detail'] = error['mistake_detail']
        tmp['user_name'] = request.user
        tmp['file_name'] = curr_task_name
        tmp['mistake_type'] = error['mistake_type']
        tmp['mistake_grade'] = error['mistake_grade']
        tmp['time'] = error['find_time']
        tmp['other'] = '无'
        error_list.append(tmp)
        i += 1
    table_errors_graph = []
    attribute_errors_graph = []
    for i in table_errors_dict:
        table_errors_graph.append({'value': table_errors_dict[i], 'name': i})
    for i in attribute_errors_dict:
        attribute_errors_graph.append({'value': attribute_errors_dict[i], 'name': i})
    data['list'] = error_list
    data['info'] = info
    data['graph_data'] = {'table': table_errors_graph, 'attribute': attribute_errors_graph}
    return render(request, 'report.html', data)


@login_required(login_url='/')
def report_detail(request, mistake_id):
    mis = mistake_service.get_mistake_by_id(mistake_id)[0]
    task_id = mis['task_id']
    tmp_task = task_service.get_task_by_task_id(task_id)[0]
    res = {}
    menu = ['错误名称', '错误级别', '错误类型', '错误描述', '详细信息', '解决方案']
    mistake_name = tmp_task['file_name'][21:]
    mistake_grade = mis['mistake_grade']
    mistake_type = mis['mistake_type']
    mistake_discription = ''
    mistake_detail = mis['mistake_detail']
    method = mis['method']
    info = {'错误名称': mistake_name, '错误级别': mistake_grade, '错误类型': mistake_type, '错误描述': mistake_discription,
            '详细信息': mistake_detail, '解决方案': method}
    res['info'] = info
    print(mis)
    print(tmp_task)
    return render(request, 'detail.html', res)
