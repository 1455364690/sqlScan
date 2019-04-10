# _*_ coding:utf-8 _*_
import datetime
from django_web import models
from django_web.const.task_state import TaskState


def create_task(user_id, file_name):
    curr_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    models.task.objects.create(user_id=user_id, file_name=file_name, create_time=curr_time, state=TaskState.INIT.value)
    return


def get_task_by_user_id(user_id):
    return models.task.objects.filter(user_id=user_id)


def get_task_by_task_id(task_id):
    return models.task.objects.filter(id=task_id).values()


def save_error(task_id, mistake_type, mistake_grade, mistake_detail, find_time, method, extends):
    models.mistake.objects.create(task_id=task_id, mistake_type=mistake_type, mistake_grade=mistake_grade,
                                  mistake_detail=mistake_detail, find_time=find_time, method=method, extends=extends)


def get_error(task_id):
    return models.mistake.objects.filter(task_id=task_id).values()


def start_task():
    pass
