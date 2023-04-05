
from django.urls import path, re_path
from .views import (product_list_view, product_detail, HomeView, AboutView)


app_name = 'buyer'
urlpatterns = [
    #path('', MenuView.as_view(), name='menu'),
    path('', HomeView.as_view(), name='home'),
    path('about', AboutView.as_view(), name='about'),
    # re_path('signup/?', SignupView.as_view(), name='signup'),
    # re_path('login/?', LoginView.as_view(), name='login'),
    # path('logout/', logout_view, name='logout'),
    # re_path('create/?', seller_create, name='create_product'),
    # path('', ProductListView.as_view(), name='products_list'),
    path('products', product_list_view, name='products_list'),
    # re_path (r'^(?P<slug>[\w-]+)', product_detail, name='product_detail'),
    path('<slug:slug>/', product_detail, name='product_detail'),
]
