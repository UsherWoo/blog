'''
home/views01.py
'''
from django.shortcuts import render,redirect
from datetime import datetime
from home.models import Post            #匯入自訂資料模組

def homepage(request):                  #定義網頁函式
    posts = Post.objects.all()
    now = datetime.now()
    return render(request,'index.html',locals())

def showPost(request,slug):
    try:
        post = Post.objects.get(slug = slug)
        if post != None:
            return render(request, 'post.html', locals())
    except:
        return redirect('/')

