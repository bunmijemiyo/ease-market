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
    # path('reg', logint_view, name='reg' ),
    # path('home', ProfileView.as_view(), name='home'),
    path('products', seller_view, name='my_products'),
    # re_path('signup/?', SignupView.as_view(), name='signup'),
    # re_path('login/?', LoginView.as_view(), name='login'),
    # path('logout/', logout_view, name='logout'),
    # path('logv/?', login_views, name='logv'),
    # re_path('create/?', seller_create, name='create_product'),
    # path('list', SellerListView.as_view(), name='seller_list'),
    # re_path (r'^(?P<slug>[\w-]+)', seller_detail, name='detail'),
    path('logout/', logout_view, name='logout'),
]