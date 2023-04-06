from django.urls import path, re_path
from django.contrib.auth.views import LogoutView
# from .views import (logint_view, login_views, ProfileView, LoginView, logout_view, SignupView, seller_create, SellerListView, seller_detail, registration_view)
from .views import (registration_view, login_view, createProduct, seller_view, logout_view)

app_name = 'seller'
urlpatterns = [
    #path('', MenuView.as_view(), name='menu'),
    path('regis', registration_view, name='signup' ),
    path('login', login_view, name='login' ),
    path('create', createProduct, name='create' ),
    path('products', seller_view, name='my_products'),
    path('logout/', logout_view, name='logout'),
]