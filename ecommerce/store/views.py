from django.shortcuts import render
from django.http import HttpResponse
from .models.product import Product
from .models.category import Category
from .models.costumer import Costumer

def index(request):
    products=None
    category=Category.get_all_categories();
    
    categoryID = request.GET.get('category')
    if categoryID:
        products= Product.get_all_product_by_category_id(categoryID)
    else:
        products= Product.get_all_products()
    
    data={}
    data['product']=products
    data['category']=category
    return render(request, 'index.html', data)

def signup(request):
    
    if request.method=='GET':
        return render(request, 'signup.html')
    else:
        postData=request.POST
        name=postData.get('name')
        phone=postData.get('phone')
        
        costumer=Costumer(name=name,
                          phone=phone)
        costumer.register()
        return HttpResponse("Sukses Signup")
    
