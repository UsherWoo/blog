'''
    home/admin.py
'''
from django.contrib import admin

# Register your models here.
from home.models import Post,Product,Channel
from home.models import Phone,PhoneMaker,PhoneModel,PhonePhoto

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','pub_date')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('sku','name','price','size')

class ChannelAdmin(admin.ModelAdmin):
    list_display = ('name','code')

admin.site.register(Post,PostAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Channel,ChannelAdmin)
admin.site.register(Phone)
admin.site.register(PhoneMaker)
admin.site.register(PhoneModel)
admin.site.register(PhonePhoto)
