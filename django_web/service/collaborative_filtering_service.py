# coding:utf-8
from math import *
from django_web.service import file_service
from django_web.service import user_service
from django_web.service import task_service
import datetime


def get_similarity(new_tables, old_tables):
    distance = 1
    for i in new_tables:
        if i not in old_tables:
            distance += 1
    for i in old_tables:
        if i not in new_tables:
            distance += 1
    return 1 / float(distance)


def get_error_tables(new_tables, tables_times):
    res = []
    tables_in_his = {}
    for i in tables_times:
        if i not in new_tables:
            tables_in_his[i] = tables_times[i]
    for i in new_tables:
        if i not in tables_times.keys():
            tables_in_his[i] = 0
    for i in tables_in_his:
        data = {'sim': tables_in_his[i], 'table_name': i}
        if tables_in_his[i] >= 9:
            data['message'] = '高危'
        elif tables_in_his[i] >= 6:
            data['message'] = '中危'
        elif tables_in_his[i] >= 3:
            data['message'] = '低危'
        elif tables_in_his[i] == 0:
            data['message'] = '多余'
        else:
            data['message'] = '普通'
        res.append(data)
    return res


def get_table_list(history, similar_table_key):
    table_dict = {}
    res = []
    """
    给定相似度最高几个套餐名，获取其中的包含的数据库表
    :param history:历史套餐数据
    :param similar_table_key:相似度最高的套餐的key，即套餐名
    :return:
    """
    for i in history:
        table_dict[i['name']] = i['tables']
    for i in similar_table_key:
        res.append(table_dict.get(i[0]))
    return res


def get_similar_tables_times(similar_tables_list):
    """
    获取相似套餐中所有表的出现次数
    :param similar_tables_list:
    :return:
    """
    tables_times = {}
    for tables in similar_tables_list:
        for table in tables:
            tables_times[table] = tables_times.get(table, 0) + 1
    # print(tables_times)
    return tables_times


def start(package):
    # 获取历史套餐数据
    history_map = file_service.get_history_tables()
    history = history_map['data']
    # 计算历史套餐与新套餐的相似度
    sims = []
    for his in history:
        sim = get_similarity(package['tables'], his['tables'])
        sims.append((his['name'], sim))
    # 将相似度从大到小排列
    sims.sort(key=lambda x: x[1], reverse=True)
    # 获取相似度最高的10个套餐的数据库表
    similar_tables_list = get_table_list(history, sims[:10])
    # 计算相似度最高的十个套餐中未在新套餐中出现的表出现的次数
    table_times = get_similar_tables_times(similar_tables_list)
    # 计算结果
    errors = get_error_tables(package['tables'], table_times)
    return errors


def save_errors(task_id, errors):
    tmp_task = task_service.get_task_by_task_id(task_id)[0]
    for i in errors:
        curr_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        task_service.save_error(tmp_task['id'], '数据库表错误', i['message'], i['table_name'], curr_time, '请及时解决',
                                i['sim'])
    return 0
# {'sim': 10, 'table_name': 'ucr_iupc.PM_OFFER_REL', 'message': '高危'}
# Recommendations = recommend('1')
# print(Recommendations)
