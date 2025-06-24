'''
home/views05.py
'''
from django.shortcuts import render,redirect
from datetime import datetime
Member = {'王小明':'123','b':'456'}

def login(request):    #定義網頁函式
    now = datetime.now()
    message = ''
    try:
        name = request.GET['name']
        password = request.GET['password']
    except:
        name = None       #尚未填表單
    if name != None:
        if name in Member:
            if password == Member[name]:
                message = name + ':您好'
                request.session['userName'] = name
            else:
                message = '密碼錯誤'
        else:
            message = name + ':尚未註冊'
    return render(request,'index05.html',locals())

def logout(request):
    request.session['userName'] = None
    return redirect('/') 
