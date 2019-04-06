# _*_coding:utf-8_*_

import hashlib


def md5(password):
    m = hashlib.md5()
    temp = password.encode(encoding='utf-8')
    m.update(temp)
    return m.hexdigest()

