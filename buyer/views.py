
from django.shortcuts import render, get_object_or_404
from django.views import View
#from seller.models import Seller
#from django.app import apps
# model = apps.get_model('seller', 'Seller')

from seller.models import User, Product

# Create your views here.
# class ProductListView(View):
#     def get(self, request, *args, **kwargs):
#         # items = model.objects.all()
#         items = Product.objects.all()
#         print("items", items, "product list")
#         context = {'items': items }
#         return render(request, 'buyer/all_products.html', context)

# def product_details(request, slug):
#     print(slug, "slug", "product detail")
#     #return HttpResponse(slug)
#     item = Product.objects.get(slug=slug)
#     context = {'item': item}
#     return render(request, 'buyer/product_detail.html', context)

def product_detail(request, slug):
    
    item = get_object_or_404(Product, slug=slug)
    seller = ""
    context = {}
    if item:
        seller = get_object_or_404(User, username=item.username)
        context = {'item': item,'seller': seller}
    return render(request, 'buyer/product_detail.html', context)

def product_list_view(request):
    items = Product.objects.all()
    context = {'items': items }
    return render(request, 'buyer/all_products.html', context)

class HomeView(View):

	def get(self, request, *args, **kwargs):
		return render(request, 'buyer/home.html')

class AboutView(View):

	def get(self, request, *args, **kwargs):
		return render(request, 'buyer/about.html')