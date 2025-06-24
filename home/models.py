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

#頻道類別
class Channel(models.Model):
    name = models.CharField(max_length=12)
    code = models.CharField(max_length=12)

#手機製造商類別
class PhoneMaker(models.Model):
    name = models.CharField(max_length=10)
    country = models.CharField(max_length=10)
    def __str__(self):
        return self.name

#手機型號類別
class PhoneModel(models.Model):
    maker = models.ForeignKey(PhoneMaker,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    url = models.URLField(default='')
    def __str__(self):
        return self.name

#手機類別
class Phone(models.Model):
    model = models.ForeignKey(PhoneModel,on_delete=models.CASCADE)
    name = models.CharField(max_length=15,default='超值二手機')
    description = models.TextField(default='暫無說明')
    year = models.PositiveIntegerField(default=2016)
    price = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.name

#手機圖片類別
class PhonePhoto(models.Model):
    phone = models.ForeignKey(Phone,on_delete=models.CASCADE)
    description = models.CharField(max_length=20,default='產品照片')
    url = models.URLField(default='localhost')
    media = models.CharField(max_length=100,default='non')
    def __str__(self):
        return self.description 
