# _*_coding:utf-8 _*_
from django.shortcuts import render


def get_report(request, task_id):
    if request.method == 'POST':
        print("post")
    else:
        print("get")
    return render(request, 'report.html')
