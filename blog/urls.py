"""
blog/urls.py
"""
from django.contrib import admin            #匯入管理模組
from django.urls import path                #匯入網址模組
from home.views01 import homepage,showPost  #匯入自訂網頁模組

urlpatterns = [
    path('', homepage),             #根目錄，呼叫homepage函式
    path('admin/', admin.site.urls),#管理目錄，呼叫公版網址
    path('post/<slug:slug>',showPost)
]
