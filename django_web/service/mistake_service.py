# _*_ coding:utf:8 _*_
from django_web import models


def get_mistake_by_id(mistake_id):
    return models.mistake.objects.filter(id=mistake_id).values()


