# _*_ coding:utf-8 _*_

import datetime


def upload_file(file):
    file_dir = 'static/file/'
    res_map = {}
    try:
        file_name = str(datetime.datetime.now().strftime('_%Y_%m_%d_%H_%M_%S_')) + file.name
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


def read_file(file):
    pass


def delete_file(file):
    pass
