'''
    homw/admin.py
'''
from django.contrib import admin

# Register your models here.
from home.models import Post,Product

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','pub_date')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('sku','name','price','size')

admin.site.register(Post,PostAdmin)
admin.site.register(Product,ProductAdmin)
