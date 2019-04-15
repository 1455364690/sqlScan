# _*_ coding:utf-8 _*_

import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django_web.service import apriori_service

from django_web.service import user_service


def user_login(request):
    # apriori_service.start_apriori('ucr_iupc.PM_OFFER_REL', 'REL_OFFER_ID')
    if request.method == 'POST':
        body = json.loads(request.body)
        username = body.get('username')
        password = body.get('password')
        user_service.get_all_common_users()
        res = user_service.user_login(request, username, password)
        return HttpResponse(json.dumps(res), content_type='application/json')


@login_required(login_url='/')
def user_logout(request):
    res = user_service.user_logout(request)
    return HttpResponse(json.dumps(res), content_type='application/json')


def user_reg(request):
    if request.method == "POST":
        body = json.loads(request.body)
        username = body.get('username')
        password = body.get('password')
        success = user_service.create_user(username, password)
        if success:
            res = {'code': 0, 'message': '注册成功'}
            return HttpResponse(json.dumps(res), content_type='application/json')
        else:
            res = {'code': 1, 'message': '用户已存在'}
            return HttpResponse(json.dumps(res), content_type='application/json')


@login_required(login_url='/')
def admin_user(request):
    common_users = user_service.get_all_common_users()
    users = []
    menu = ['编号', '用户id', '用户名', '用户注册时间', '用户状态', '操作']
    k = 0
    for i in common_users:
        k += 1
        tmp = {}
        tmp['id'] = k
        tmp['user_id'] = i['id']
        tmp['username'] = i['name']
        tmp['create_time'] = i['create_time']
        tmp['state'] = i['user_state']
        users.append(tmp)
    data = {'users': users, 'menu': menu}
    return render(request, 'admin.html', data)


@login_required(login_url='/')
def react_user(request):
    body = json.loads(request.body)
    user_id = body.get('user_id')
    res = user_service.react_user(user_id)
    return HttpResponse(json.dumps(res), content_type='application/json')


@login_required(login_url='/')
def freeze_user(request):
    body = json.loads(request.body)
    user_id = body.get('user_id')
    res = user_service.freeze_user(user_id)
    return HttpResponse(json.dumps(res), content_type='application/json')
