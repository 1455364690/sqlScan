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
    User.objects.create_user(username=username, password=password, email='null')
    models.user.objects.create(username=username, password=hashers.make_password(password), create_time=curr_time,
                               modify_time=curr_time)


def get_user_by_id(user_id):
    tmp_user = User.objects.filter(id=user_id)
    return tmp_user.values()


def get_user_by_name(user_name):
    tmp_user = User.objects.filter(username=user_name)
    return tmp_user.values()


def user_login(request, username, password):
    tmp_user = auth.authenticate(username=username, password=password)
    res = {}
    if tmp_user:
        res['code'] = 0
        res['message'] = '登录成功'
        login(request, tmp_user)
    else:
        res['code'] = 1
        res['message'] = '登录失败'
        res['user'] = None
    return res
