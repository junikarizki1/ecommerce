from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.costumer import Costumer

class AdminProduct(admin.ModelAdmin):
    list_display=['id','name','price','category','description']
    
class AdminCostumer(admin.ModelAdmin):
    list_display=['id','name','phone']

admin.site.register(Product, AdminProduct)
admin.site.register(Category)
admin.site.register(Costumer, AdminCostumer)