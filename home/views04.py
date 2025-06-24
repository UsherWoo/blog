'''
home/views04.py
'''
from django.shortcuts import render
from datetime import datetime
from home.models import Phone,PhonePhoto

def homepage(request):    #定義網頁函式
    now = datetime.now()
    phone_list = Phone.objects.all()
    return render(request,'index04.html',locals())

def showPhone(request,id):
    try:
        phone = Phone.objects.get(id = id)
        photos = PhonePhoto.objects.filter(phone=phone)
    except Phone.DoesNotExist:
        pass #raise Http404('找不到指定的品項編號')
    return render(request, 'phone.html', locals())
