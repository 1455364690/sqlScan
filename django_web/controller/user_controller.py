# _*_ coding:utf-8 _*_

import json

from django.http import HttpResponse

from django_web.service import user_service


def user_login(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        username = body.get('username')
        password = body.get('password')
        res = user_service.user_login(request, username, password)
        return HttpResponse(json.dumps(res), content_type='application/json')


def user_logout():
    return
