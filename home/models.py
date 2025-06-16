'''
home/models.py
'''
from django.db import models

# Create your models here.
# 文章類別
class Post(models.Model):   #建立資料表
    title = models.CharField(max_length=200)
    slug  = models.CharField(max_length=200)
    body  = models.TextField()
    pub_date  = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-pub_date',)
    def __str__(self):
        return self.title

# 產品類別
class Product(models.Model):
    SIZES=(
        ('S','Small'),
        ('M','Medium'),
        ('L','Large'),
    )
    sku = models.CharField(max_length=5) #存貨單位(stock keeping unit)
    name = models.CharField(max_length=20)
    price = models.PositiveIntegerField()            #正整數
    size = models.CharField(max_length=1,choices=SIZES) #選單
    class Meta:
        ordering = ('sku',)
    def __str__(self):
        return self.name
