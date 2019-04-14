# _*_ coding:utf-8 _*_

import datetime
import os
import re
from demo.settings import STATICFILES_DIRS

file_dir = 'static/file/'


def upload_file(file):
    """
    上传文件
    :param file:
    :return:
    """
    res_map = {}
    file_name = str(datetime.datetime.now().strftime('_%Y_%m_%d_%H_%M_%S_')) + file.name
    try:
        des = open(file_dir + file_name, 'wb+')
        for chunk in file.chunks():
            des.write(chunk)
        res_map['code'] = 0
        res_map['message'] = '文件上传成功'
        res_map['file_name'] = file_name
    except Exception as e:
        res_map['code'] = 1
        res_map['message'] = '文件上传失败'
        res_map['detail'] = e
        res_map['file_name'] = file_name
    return res_map


def read_file(file_name, file_path=file_dir):
    """
    读取文件
    :param file_name:
    :param file_path:
    :return:
    """
    data = {}
    tmp_str = ''
    try:
        file = open(file_path + file_name, 'r', encoding='UTF-8')
        line = file.readline()
        while line:
            tmp_str += line
            line = file.readline()
        file.close()
        data['code'] = 0
        data['message'] = '文件' + file_name + '读取成功'
        data['data'] = tmp_str
    except Exception as e:
        try:
            file = open(file_path + file_name, 'r', encoding='GBK')
            line = file.readline()
            while line:
                tmp_str += line
                line = file.readline()
            file.close()
            data['code'] = 0
            data['message'] = '文件' + file_name + '读取成功'
            data['data'] = tmp_str
        except Exception as  e:
            data['code'] = 1
            data['message'] = '文件' + file_name + '读取失败'
            data['detail'] = e
            data['data'] = None
    return data


def delete_file(file):
    pass


def get_tables(sql_str):
    """
    从SQL语句中找出所有表名
    :param sql_str:
    :return:
    """
    res = re.findall(r"insert into (.+?) ", sql_str, re.S)
    if res is None or len(res) == 0:
        res = re.findall(r"INSERT INTO (.+?) ", sql_str, re.S)
    data = []
    for i in res:
        if i not in data:
            data.append(i)
    return data


def get_history_tables():
    """
    从历史套餐中获取数据库表名
    :return:
    """
    path = os.path.join(STATICFILES_DIRS[0], 'file', 'history_tables/')
    file_names = os.listdir(path)
    res = {}
    data = []
    for file_name in file_names:
        history_file_map = read_file(file_name, path)
        if history_file_map['code'] != 0:
            res['code'] = 1
            res['message'] = '历史套餐文件读取失败'
            return res
        history_file = history_file_map['data']
        tables = get_tables(history_file)
        data.append({'name': file_name, 'tables': tables})
    res['code'] = 0
    res['data'] = data
    return res


def get_all_insert_sql(sql_str):
    """
    读取一个sql文件中所有的insert命令
    :param sql_str:
    :return: ['','',''....]
    """
    try:
        res = re.findall(r"insert into [\s\S]+?\);", sql_str, re.S)
        return res
    except Exception as e:
        print(str(e))
        return None


def get_insert_sql_info_by_attribute(insert_sql, attribute):
    """
    读取insert语句中的属性值和数值的对应关系
    :param insert_sql:
    :return:
    """
    count = 0
    index = 0
    left = []
    for i in insert_sql:
        if i == '(':
            count += 1
            left.append(index)
            if count == 2:
                break
        index += 1
    right = insert_sql.find(')')
    attrs_str = insert_sql[left[0] + 1:right]
    values_str = insert_sql[left[1] + 1:len(insert_sql) - 2]
    tmp_a = attrs_str.split(',')
    tmp_b = values_str.split(',')
    attrs = []
    values = []
    for i in tmp_a:
        i = i.strip()
        attrs.append(i)
    for i in tmp_b:
        i = i.strip()
        values.append(i[1: len(i) - 1])
    # dictionary:{a:b,c:d......}
    dictionary = dict(map(lambda x, y: [x, y], attrs, values))
    for i in dictionary:
        if i == attribute:
            return dictionary[i]
    return None


def get_values_by_table_and_attribute_key(table_name, attribute_key):
    """
    根据数据库表名和关键属性获取所有数值的列表
    :param table_name: 数据库表名
    :param attribute_key: 关键属性名
    :return: [[,,,,],[,,,,],[,]]
    """
    path = os.path.join(STATICFILES_DIRS[0], 'file', 'history_tables/')
    file_names = os.listdir(path)
    res = {}
    value_lists = []
    # 读取所有文件
    for file_name in file_names:
        # 读取文件
        value_list = []
        history_file_map = read_file(file_name, path)
        if history_file_map['code'] != 0:
            res['code'] = 1
            res['message'] = '历史套餐文件读取失败'
            return res
        else:
            # 获取全部的insert命令
            insert_list = get_all_insert_sql(history_file_map['data'])
            if insert_list is None:
                print("查找失败")
            for i in insert_list:
                # 表名
                tmp_table_name = get_tables(i)[0]
                if tmp_table_name != table_name:
                    continue
                # value_list:[]
                value_list.append(get_insert_sql_info_by_attribute(i, attribute_key))
        value_lists.append(value_list)
    return value_lists
