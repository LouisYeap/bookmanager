from django.shortcuts import render

# Create your views here.

# 视图函数第一个参数就是接收请求，

from django.http import HttpRequest
from django.http import HttpResponse


def index(request):
    # render：渲染
    context = {
        'name': "Give you  a gift when you click me "
    }
    return render(request, 'book/index.html', context=context)
