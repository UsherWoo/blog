'''
home/views01.py
'''
from django import forms
from django.core.paginator import Paginator
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

class PostForm(forms.ModelForm): #繼承ModelForm表單模組
    class Meta:
        model = Post    # model,fields 變數名稱不能擅改
        fields = ['title','slug','body']
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = '主旨'
        self.fields['slug'].label = 'slug'
        self.fields['body'].label = '本文'

def homepage(request):                  #定義網頁函式
    allPosts = Post.objects.all()
    paginator = Paginator(allPosts, 5)  # Show 5 posts per page.
    page_number = request.GET.get("page")
    posts = paginator.get_page(page_number)
    now = datetime.now()
    return render(request,'index.html',locals())

def showPost(request,id):
    try:
        post = Post.objects.get(id = id)
        if post != None:
            return render(request, 'post.html', locals())
    except:
        return redirect('/')

def addPost(request):
    if request.method == 'POST':
        postForm = PostForm(request.POST)
        if postForm.is_valid():
            postForm.save()
            return redirect('/')
    else:
        postForm = PostForm()    
    return render(request,'postadd.html',locals())
    
def delPost(request):
    if request.method == 'POST':
        selected_ids = request.POST.getlist('selected_items')
    for id in selected_ids: 
        post = Post.objects.get(id = id)
        post.delete()
    return redirect('/')

def about(request):
    me = student()
    quote = random.choice(quotes)
    return render(request,'about.html',locals())
