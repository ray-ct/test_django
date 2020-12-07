from django.contrib import auth
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def login(request):
    return render(request,'login.html')



@login_required
def index(request):
  return HttpResponse("index页面。。。")


def login_in(request):
    if request.method == "POST":
        user = request.POST.get("username")
        pwd = request.POST.get("password")
        # 验证成功，返回user对象，否则返回None
        user1 = auth.authenticate(username=user, password=pwd)
        print(user1)
        if user1:
            auth.login(request, user1)  # session写操作
            #return HttpResponse('success')
            return redirect('/index')
        else:
            return HttpResponse('fail')

    return HttpResponse('get method')
