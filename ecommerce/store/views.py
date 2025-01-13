from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

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
        
        error_message = None
        
        value = {
            'name':name,
            'phone':phone
        }
        
        costumer=Costumer(name=name,
                          phone=phone)
        
        if not name:
            error_message="Silahkan masukkan Nama terlebih dahulu"
        elif not phone:
            error_message="Silahkan masukkan Nomor HP terlebih dahulu"
        elif len(phone)<10:
            error_message="Masukkan nomor telepon yang benar"
        elif costumer.isExists():
            error_message="Nomor telepon telah terdaftar"
        if not error_message:
            messages.success(request, 'Selamat Akun Anda Berhasil Dibuat, silahkan Login')
            costumer.register()
            return redirect('signup')
        else:
            data = {
                'error':error_message,
                'value':value
            }
            return render(request, 'signup.html', data)

def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        phone = request.POST.get('phone')
        error_message = None
        value ={
            'phone':phone
        }
        costumer = Costumer.objects.filter(phone=request.POST["phone"])
        if costumer:
            return redirect('home') 
        else:
            error_message = "Nomor telepon tidak terdaftar"
            data = {
                'error':error_message,
                'value':value
            }
        return render(request, 'login.html',data)
    
