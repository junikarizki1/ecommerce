from django.contrib import admin
from django.urls import path
from store import views

urlpatterns = [
    path('',views.index, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/',views.login, name='login'),
    path('product/<str:product_code>/', views.product_detail, name='product_detail'),
    path('product_list/',views.product_list, name='product_list'),
]
