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
    mistake_description = ''
    mistake_detail = mis['mistake_detail']
    method = mis['method']
    if mistake_type == '数据库表错误':
        if mistake_grade == '高危':
            mistake_name = '数据库表[  '+mis['mistake_detail']+'  ]极有可能被遗漏'
            mistake_description = '数据库表高危错误，与该套餐最相似的10个历史套餐中，有9个及以上的套餐使用到了该数据库表，而新创建的套餐未使用到。'
            method = '该错误为高危错误，极有可能导致创建错误套餐，希望套餐业务员可以慎重核实该套餐是否涉及到本表，如果遗漏请尽快修补有关本数据库表的sql语句。'
        elif mistake_grade == '中危':
            mistake_name = '数据库表[  ' + mis['mistake_detail'] + '  ]很有可能被遗漏'
            mistake_description = '数据库表中危错误，与该套餐最相似的10个历史套餐中，有6个至8个的套餐使用到了该数据库表，而新创建的套餐未使用到。'
            method = '该错误为中危错误，很有可能导致创建错误套餐，希望套餐业务员可以慎重核实该套餐是否涉及到本表，如果遗漏请尽快修补有关本数据库表的sql语句。'
        elif mistake_grade == '低危':
            mistake_name = '数据库表[  ' + mis['mistake_detail'] + '  ]有可能被遗漏'
            mistake_description = '数据库表低危错误，与该套餐最相似的10个历史套餐中，有3个至5个的套餐使用到了该数据库表，而新创建的套餐未使用到。'
            method = '该错误为低危错误，有可能导致创建错误套餐，希望套餐业务员可以慎重核实该套餐是否涉及到本表，如果遗漏请尽快修补有关本数据库表的sql语句。'
        elif mistake_grade == '多余':
            mistake_name = '数据库表[  ' + mis['mistake_detail'] + '  ]有可能多余'
            mistake_description = '数据库表多余错误，与该套餐最相似的10个历史套餐中，均未使用到该数据库表，而新创建的套餐使用到了该表。'
            method = '该错误为低危错误，有可能导致创建错误套餐，希望套餐业务员可以慎重核实该套餐是否涉及到本表，如果遗漏请尽快修补有关本数据库表的sql语句。'
            pass
    elif mistake_type == '关键属性错误':
        pass
    info = {'错误名称': mistake_name, '错误级别': mistake_grade, '错误类型': mistake_type, '错误描述': mistake_description,
            '详细信息': mistake_detail, '解决方案': method}
    res['info'] = info
    print(mis)
    print(tmp_task)
    return render(request, 'detail.html', res)
