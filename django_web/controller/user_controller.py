# _*_ coding:utf-8 _*_

import json

from django.http import HttpResponse

from django_web.service.check_login_service import check_login


def user_login(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        username = body.get('username')
        password = body.get('password')
        res = check_login(username, password)
        return HttpResponse(json.dumps(res), content_type='application/json')
