# _*_ coding:utf-8 _*_
import datetime
from django_web.models import task
from django_web.const.task_state import TaskState


def create_task(user_id, file_name):
    curr_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    task.objects.create(user_id=user_id, file_name=file_name, create_time=curr_time, state=TaskState.INIT.value)
    return


def get_task_by_user_id(user_id):
    return task.objects.filter(user_id=user_id)


def get_task_by_task_id(task_id):
    return task.objects.filter(id=task_id).values()


def start_task():
    pass
