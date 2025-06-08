'''
home/views.py
'''
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse    #匯入公版網頁模組
from home.models import Post            #匯入自訂資料模組

def homepage(request):                  #定義網頁函式
    posts = Post.objects.all()
    lists = list()
    for index,post in enumerate(posts,start=1): #讀取資料
        s = "<p>"
        s+= f"No.{index:02d}:" + str(post) + "<hr>"
        s+= post.body + "</p>"
        lists.append(s)
    return HttpResponse(lists)
