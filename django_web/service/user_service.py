# _*_ coding:utf-8 _*_
from django_web import models
from django.contrib import auth
from django_web.service import md5_service
from django.contrib.auth import login
from django.contrib.auth import hashers
from django.contrib.auth.models import User
import datetime


def create_user(username, password):
    """
    用户注册，在两个表中都创建用户信息
    :param username: 用户名
    :param password: 密码
    :return:
    """
    curr_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    check = get_user_by_name(username)
    if len(check) == 0:
        User.objects.create_user(username=username, password=password, email='null')
        models.user.objects.create(name=username, password=hashers.make_password(password), create_time=curr_time,
                                   modify_time=curr_time, user_role=1, user_state=0)
        return True
    else:
        return False


def get_user_by_id(user_id):
    tmp_user = models.user.objects.filter(id=user_id)
    return tmp_user.values()


def get_user_by_name(user_name):
    tmp_user = models.user.objects.filter(name=user_name)
    return tmp_user.values()


def get_all_common_users():
    users = models.user.objects.all().values()
    common_users = []
    for tmp_user in users:
        if not tmp_user['user_role'] == 0:
            common_users.append(tmp_user)
    return common_users


def user_logout(request):
    """
    用户注销
    :param request:
    :return:
    """
    try:
        auth.logout(request)
        res = {'code': 0, 'message': '注销成功'}
        return res
    except Exception as e:
        res = {'code': 1, 'message': '注销失败', 'detail': str(e)}
        return res


def user_login(request, username, password):
    tmp_user_name = auth.authenticate(username=username, password=password)
    res = {}
    if tmp_user_name:
        tmp_user = get_user_by_name(tmp_user_name)
        user_state = tmp_user[0]['user_state']
        if user_state == 0:
            res['code'] = 2
            res['message'] = '改用户处于冻结状态，请联系管理员激活'
            res['user'] = None
        else:
            res['code'] = 0
            res['message'] = '登录成功'
            role = tmp_user[0]['user_role']
            res['role'] = role
            login(request, tmp_user_name)
    else:
        res['code'] = 1
        res['message'] = '登录失败'
        res['user'] = None
    return res


def react_user(user_id):
    """
    激活用户
    :param user_id:
    :return:
    """
    try:
        models.user.objects.filter(id=user_id).update(user_state=1)
        return {'code': 0, 'message': '激活成功'}
    except Exception as e:
        return {'code': 1, 'message': '激活失败', 'detail': str(e)}


def freeze_user(user_id):
    """
    冻结用户
    :param user_id:
    :return:
    """
    try:
        models.user.objects.filter(id=user_id).update(user_state=0)
        return {'code': 0, 'message': '冻结成功'}
    except Exception as e:
        return {'code': 1, 'message': '冻结失败', 'detail': str(e)}
