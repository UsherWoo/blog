"""
blog/urls.py
"""
from django.contrib import admin                 #匯入管理模組
from django.urls import path                     #匯入網址模組
from home.views01 import homepage,showPost,about #匯入自訂網頁模組
from home.views02 import homepage02,showProduct

urlpatterns = [
    path('',homepage),         #根目錄，呼叫homepage函式
    path('admin/', admin.site.urls),    #管理目錄，呼叫公版網址
    path('post/<str:slug>',showPost),
    path('about/', about),
    path('product/', homepage02),
    path('product/<str:sku>', showProduct)
]
