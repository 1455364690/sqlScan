# _*_ coding:utf-8 _*_
from django_web import models


def get_user_by_id(user_id):
    tmp_user = models.user.objects.filter(id=user_id)
    return tmp_user.values()


def get_user_by_name(user_name):
    tmp_user = models.user.objects.filter(user_name=user_name)
    return tmp_user.values()
