# _*_ coding:utf-8 _*_

import datetime
import os
import re
from demo.settings import STATICFILES_DIRS

file_dir = 'static/file/'


def upload_file(file):
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
    data = {}
    str = ''
    try:
        file = open(file_path + file_name, 'r', encoding='UTF-8')
        line = file.readline()
        while line:
            str += line
            line = file.readline()
        file.close()
        data['code'] = 0
        data['message'] = '文件' + file_name + '读取成功'
        data['data'] = str
    except Exception as e:
        try:
            file = open(file_path + file_name, 'r', encoding='GBK')
            line = file.readline()
            while line:
                str += line
                line = file.readline()
            file.close()
            data['code'] = 0
            data['message'] = '文件' + file_name + '读取成功'
            data['data'] = str
        except Exception as  e:
            data['code'] = 1
            data['message'] = '文件' + file_name + '读取失败'
            data['detail'] = e
            data['data'] = None
    return data


def delete_file(file):
    pass


def get_tables(sql_str):
    res = re.findall(r"insert into (.+?) ", sql_str, re.S)
    if res is None or len(res) == 0:
        res = re.findall(r"INSERT INTO (.+?) ", sql_str, re.S)
    data = []
    for i in res:
        if i not in data:
            data.append(i)
    return data


def get_history_tables():
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

