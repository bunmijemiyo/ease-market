
from django.urls import path, re_path
from .views import (product_list_view, product_detail, HomeView, AboutView)


app_name = 'buyer'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about', AboutView.as_view(), name='about'),
    
    path('products', product_list_view, name='products_list'),
    path('<slug:slug>/', product_detail, name='product_detail'),
]
