'''
home/views03.py
'''
from django.http import Http404
from django.shortcuts import render
from datetime import datetime
from home.models import Channel #匯入自訂資料模組

def homepage(request,tv_no = 0):    #定義網頁函式
    now = datetime.now()
    tv_list = Channel.objects.all()
    tv = tv_list[tv_no] 
    return render(request,'index03.html',locals())

