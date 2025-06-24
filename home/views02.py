'''
home/views02.py
'''
from django.http import Http404
from django.shortcuts import render
from datetime import datetime
from home.models import Product #匯入自訂資料模組

def homepage(request):                  #定義網頁函式
    products = Product.objects.all()
    now = datetime.now()
    return render(request,'index02.html',locals())

def showProduct(request,sku):
    try:
        product = Product.objects.get(sku = sku)
    except Product.DoesNotExist:
        raise Http404('找不到指定的品項編號')
    return render(request, 'product.html', locals())
