"""
blog/urls.py
"""
from django.contrib import admin                 #匯入管理模組
from django.urls import path                     #匯入網址模組
from home import views01                     #匯入自訂網頁模組
from home import views02
from home import views03
from home import views04
from home import views05

urlpatterns = [
    path('',views01.homepage),        #根目錄，呼叫homepage函式
    path('admin/', admin.site.urls),  #管理目錄，呼叫公版網址
    path('post/<int:id>',views01.showPost),
    path('post/add/',views01.addPost),
    path('post/del/',views01.delPost),
    path('about/', views01.about),
    path('product/', views02.homepage),
    path('product/<str:sku>', views02.showProduct),
    path('video/<int:tv_no>', views03.homepage, name='tv-url'),
    path('phone/', views04.homepage),
    path('phone/<int:id>', views04.showPhone, name='phone-url'),
    path('login/', views05.login),
    path('logout/', views05.logout)
]
