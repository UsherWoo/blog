'''
home/views01.py
'''
from django.shortcuts import render,redirect
from datetime import datetime
from home.models import Post            #匯入自訂資料模組
import random

#.html檔,皆放在template所設定的路徑下
#而template路徑,則在blog/settings.py中設定

class student:
    name = 'Usher'
    no = 'D11234567'
    school = '健行科大'
    dep = '資訊工程'

quotes = [
    '今日事,今日畢',
    '要怎麼收獲,先怎麼栽',
    '知識就是力量',
    '讀萬卷書。行萬里路'
]
#quote = random.choice(quotes)

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

def about(request):
    me = student()
    quote = random.choice(quotes)
    return render(request,'about.html',locals())
