# _*_coding:utf-8_*_
from django_web.models import *
from django_web.service.md5_service import *
from django.contrib.auth import authenticate


def check_login(username, password):
    md5_password = md5(password)
    tmp_users = user.objects.filter(name=username)
    res = {}
    if tmp_users is None:
        res['code'] = 1
        res['message'] = '用户不存在'
        print(res)
        return res
    if len(tmp_users) == 0:
        res['code'] = 1
        res['message'] = '用户不存在'
        return res
    if md5_password == tmp_users[0].password:
        res['code'] = 0
        res['message'] = '登录成功'
        return res
    else:
        res['code'] = 2
        res['message'] = '密码错误'
        return res
