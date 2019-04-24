# _*_ coding:utf-8 _*_
import datetime
from django_web import models
from django_web.const.task_state import TaskState
from django_web.service import file_service
from django_web.service import collaborative_filtering_service
from django_web.service import apriori_service


def create_task(user_id, file_name):
    curr_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    models.task.objects.create(user_id=user_id, file_name=file_name, create_time=curr_time, state=TaskState.INIT.value)
    return


def get_task_by_user_id(user_id):
    return models.task.objects.filter(user_id=user_id)


def get_task_by_task_id(task_id):
    return models.task.objects.filter(id=task_id).values()


def save_error(task_id, mistake_type, mistake_grade, mistake_detail, find_time, method, extends, similar_files,
               files_has_table):
    new_similar_files = ''
    new_files_has_table = ''
    for i in similar_files:
        new_similar_files += ','+i
    for i in files_has_table:
        new_files_has_table += ','+i
    models.mistake.objects.create(task_id=task_id, mistake_type=mistake_type, mistake_grade=mistake_grade,
                                  mistake_detail=mistake_detail, find_time=find_time, method=method, extends=extends,
                                  similar_files=new_similar_files[1:], error_lines=new_files_has_table[1:])


def get_table_error(task_id):
    return models.mistake.objects.filter(task_id=task_id, mistake_type='数据库表错误').values()


def get_attribute_error(task_id):
    return models.mistake.objects.filter(task_id=task_id, mistake_type='关键属性错误').values()


def task_success(task_id):
    models.task.objects.filter(id=task_id).update(state=1)


def task_fail(task_id):
    models.task.objects.filter(id=task_id).update(state=1)


def start_task(task_id, table_attribute_dict):
    res = {}
    try:
        # 获取指定的task
        temp_task = get_task_by_task_id(task_id)[0]
        # 读取文件
        file_map = file_service.read_file(temp_task['file_name'])
        # 提取文件中所有的表名 list
        tables = file_service.get_tables(file_map['data'])
        package = {'name': temp_task['file_name'], 'tables': tables}
        # 协同过滤
        errors = collaborative_filtering_service.start(package)
        # 保存错误到数据库中
        collaborative_filtering_service.save_errors(task_id, errors)
        # 获取置信度关系
        for i in table_attribute_dict:
            # 关联规则挖掘
            data = apriori_service.task_apriori_check(temp_task['file_name'], i, table_attribute_dict[i])
            # 保存错误到数据库中
            apriori_service.save_apriori_mistake(task_id, data, i, table_attribute_dict[i])
        res['code'] = 0
        res['message'] = '任务执行成功'
    except Exception as e:
        res['code'] = 1
        res['message'] = '任务执行失败'
        res['detail'] = e
    return res


def test(table_name, attribute):
    data = apriori_service.task_apriori_check(table_name, attribute)
    apriori_service.save_apriori_mistake(1, data)
