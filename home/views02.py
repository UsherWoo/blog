'''
home/views02.py
'''
from django.shortcuts import render,redirect
from datetime import datetime
from home.models import Product #匯入自訂資料模組

def homepage02(request):                  #定義網頁函式
    products = Product.objects.all()
    now = datetime.now()
    return render(request,'index02.html',locals())

def showProduct(request,sku):
    try:
        product = Product.objects.get(sku = sku)
        if product != None:
            return render(request, 'product.html', locals())
    except:
        return redirect('/')

