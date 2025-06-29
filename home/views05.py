'''
home/views05.py
'''
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as sys_login
from django.contrib.auth import logout as sys_logout
from django.contrib.auth.models import User
from datetime import datetime
Member = {
    '王小明':'123',
    'b':'456'
}

def login(request):    #定義網頁函式
    now = datetime.now()
    message = ''
    user = None
    try:
        name = request.GET['name']
        password = request.GET['password']
    except:
        name = None       #尚未填表單
    if name != None:
#       if name in Member:
#           if password == Member[name]:
#       user = authenticate(username=name,password=password)    
#       if user:
        try:
            User.objects.get(username=name)
            user = authenticate(username=name,password=password)
            if user is not None:
                message = name + ':您好'
    #           request.session['userName'] = name
                sys_login(request,user)
            else:
                message = '密碼錯誤'
        except:
#       else
            message = name + ':尚未註冊'
    return render(request,'index05.html',locals())

def logout(request):
#    request.session['userName'] = None
    sys_logout(request)
    return redirect('/') 
