from django.contrib import admin
from .models.product import Product
from .models.category import Category

class AdminProduct(admin.ModelAdmin):
    list_display=['id','name','price','category','description']
    

admin.site.register(Product, AdminProduct)
admin.site.register(Category)