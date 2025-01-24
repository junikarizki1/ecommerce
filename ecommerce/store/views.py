from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
import random

from .models.product import Product
from .models.category import Category
from .models.costumer import Costumer

def index(request):
    products=None
    products = Product.get_all_products()
    category=Category.get_all_categories()
    
    categoryID = request.GET.get('category')
    if categoryID:
        products= Product.get_all_product_by_category_id(categoryID)
    else:
        products= Product.get_all_products()
    
    data={}
    data['product']=products
    data['category']=category
    return render(request, 'index.html', data)
    # data = {
    #     'product': products,
    #     'category': category,
    # }
    # return render(request, 'index.html', data)


# def category_products(request, category_id):
#     try:
#         # Dapatkan kategori dan filter produk berdasarkan kategori
#         category = Category.objects.get(id=category_id)
#         products = Product.objects.filter(category=category)

#         data = {
#             'product': products,
#             'category': category,
#         }
#         return render(request, 'category.html', data)
#     except Category.DoesNotExist:
#         # Tangani jika kategori tidak ditemukan
#         return render(request, '404.html', {"message": "Kategori tidak ditemukan"})

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
        
        costumer=Costumer(name=name,phone=phone)
        
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

def product_list(request):
    product = Product.objects.all()  # Mengambil semua produk dari database
    
    category=Category.get_all_categories();
    categoryID = request.GET.get('category')
    if categoryID:
        products= Product.get_all_product_by_category_id(categoryID)
    else:
        products= Product.get_all_products()
    return render(request, 'product_list.html', {'product': product,'category':category,'products':products})
    
def product_detail(request, product_code):
    product = get_object_or_404(Product, product_code=product_code)
    
    # Mengambil 4 produk acak untuk rekomendasi
    recommended_products = random.sample(list(Product.objects.all()), 4)
    #end
    
    category=Category.get_all_categories();
    categoryID = request.GET.get('category')
    if categoryID:
        products= Product.get_all_product_by_category_id(categoryID)
    else:
        products= Product.get_all_products()
    
    return render(request, 'product_detail.html', {'product': product,'recommended_products':recommended_products, 'category':category, 'products':products})   
    
