from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.hashers import make_password, check_password
from .models import User, Product
from django.views import View
from django.http import HttpResponse
from django.http import HttpResponseForbidden
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def registration_view(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		password2 = request.POST.get('password2')
		fullname = request.POST.get('fullname')
		email = request.POST.get('email')
		phone = request.POST.get('phone')
		address = request.POST.get('address')
		state = request.POST.get('state')
		gender = request.POST.get('gender')

		user = get_object_or_404(User, username=username)
		if user:
			error_message = 'Username already exist'
			return render(request, 'seller/registration.html', {'error_message': error_message})

		if password != password2:
			error_message = 'Passwords do not match'
			return render(request, 'seller/registration.html', {'error_message': error_message})

		hashed_password = make_password(password)

		user = User.objects.create(
			username=username,
			password=hashed_password,
			fullname=fullname,
			email=email,
			phone=phone,
			address=address,
			state=state,
			gender=gender
		)
		user.save()

		# return redirect('login')
		# return HttpResponse('<h3>Registration successful!<h3>')
		return redirect('seller:login')
	return render(request, 'seller/registration.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            error_message = 'Username or password is incorrect'
            return render(request, 'seller/logins.html', {'error_message': error_message})

        if not check_password(password, user.password):
            error_message = 'Username or password is incorrect'
            return render(request, 'seller/logins.html', {'error_message': error_message})

        return redirect('seller:home')

    return render(request, 'seller/logins.html')

def login_viewt(request):
    print("one")
    if request.method == 'POST':
        print("two")
        username = request.POST.get('username')
        password = request.POST.get('password')
        print("a")
        user = authenticate(username=username, password=password)
        print("b")
        if user is not None:
            login(request, user)
            return redirect('home')  # replace 'home' with your desired URL
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'seller/logins.html')

# class ProfileView(View):

# 	def get(self, request, *args, **kwargs):
	
# 		user_id = request.session.get('user_id')
# 		if user_id:
# 			user = User.objects.get(id=user_id)
# 			username = user.username
# 			print(username, "current user")
# 		return render(request, 'buyer/home.html')


# @require_POST
def createProduct(request):
	if request.method == 'POST':
		product_name = request.POST.get('product_name')
		quantity = request.POST.get('quantity')
		description = request.POST.get('description')
		price = request.POST.get('price')
		image = request.FILES.get('imageUpload')
		slug = ""
		username = ""
		for i in product_name:
			if i == " ":
				i = "-"
			slug += i
		user_id = request.session.get('user_id')
		if user_id:
			user = User.objects.get(id=user_id)
			username = user.username
		else:
			return HttpResponseForbidden(status=403)


		product = Product(name=product_name, quantity=quantity, description=description, price=price, slug=slug, username=username, thumb=image)
		product.save()
		print(slug, username)
		return redirect('seller:products')
		# return HttpResponse('<h3>Registration successful!<h3>')

	return render(request, 'seller/createProduct.html')

def seller_view(request):
	user_id = request.session.get('user_id')
	if user_id:
		user = User.objects.get(id=user_id)
		items = Product.objects.filter(username=user.username)
		context = {'items': items }
		return render(request, 'buyer/all_products.html', context)
	return HttpResponseForbidden(status=403)

def logout_view(request):
	user_id = request.session.get('user_id')
	if user_id:
		# logout(request)
		del request.session[user_id]  # Remove user ID from session
		messages.success(request, 'You have been logged out.')
	return redirect('seller:login')




"""
from django.shortcuts import render, redirect
from .exceptions import RegistrationError
from django.http import Http404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from .forms import CreateSeller
from .models import Seller, Product
from django.contrib import messages


# Create your views here.
from django.views import View

def logint_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('home')
#         else:
#             return render(request, 'seller/logins.html', {'error': 'Invalid login'})
#     else:
#         return render(request, 'seller/logins.html')
	return render(request, 'seller/logins.html')


class ProfileView(View):

	def get(self, request, *args, **kwargs):
	# 	return render(request, 'seller/logins.html')
    
	# def post(self, request, *args, **kwargs):
	# 	if request.method == 'POST':
	# 		username = request.POST["username"]
	# 		password = request.POST["password"]
	# 		print(username, password)

	# 		user = authenticate(username=username, password=password)
	# 		if user is not None:
	# 			login(request, user)

	# 		if username:
	# 			if password:
	# 				login_info = Registrations.objects.filter(username=username)
	# 				if login_info:
	# 					user = username
	# 					login(request, user)
	# 					return render(request, 'buyer/home.html')

			# form = AuthenticationForm(data=request.POST)
			# if form.is_valid():
			# 	user = form.get_user()
				# log the user in


		# login_info = Registrations.objects.filter(username="sade")
		# print(login_info)
		# for i in login_info:
		# 	print(i.username, i.fullname, i.password, i.id)

		return render(request, 'buyer/home.html')


def registration_view(request):
	if request.method == 'POST':
		# username = request.POST["username"]
		fullname = request.POST["fullname"]
		gender = request.POST["gender"]
		state = request.POST["state"]
		phone = request.POST["phone"]
		country = request.POST["country"]
		address = request.POST["address"]
		email = request.POST["email"]
		# password = request.POST["password"]
		# password2 = request.POST["password2"]
		print(fullname, gender, state, phone, country, address, email)
		result = ["bunmijemiyo Nigeria Female Akwa Ibom +2349062209632 12356788 12, ajfjkrkrf bunmi.ogunjemiyo@gmail.com 1234"]
		if (("@" in email) and (len(fullname.split(" ")) >= 2)):
			# seller = Seller.objects.filter(author=username)
			# seller = Seller.objects.all()
			# login_info = Seller.objects.filter(username=username)
			# if login_info:
			# 	raise RegistrationError('Registration not successful')
			Seller.objects.create(fullname=fullname, gender=gender, state=state, phone=phone, country=country, address=address, email=email)
			# Products_2.objects.create(title=my_title, description=desc, price=amount)
			# new_seller = Registrations(username=username, fullname=fullname, gender=gender, state=state, phone=phone, country=country, address=address, email=email, password=password)
			# new_seller.save()
			print("done")
		


		


	# 	user = username
	# 	login(request, user)
	# 	form = AuthenticationForm(data=request.POST)
	# 	if form.is_valid():
	# 		user = form.get_user()
	# 		# log the user in
	# 		login(request, user)
	# 		return redirect('menu')
		
	# form = AuthenticationForm()
	# context = {'form': form}
	return render(request, 'seller/registration.html')

class RegisterPage(FormView):
	template_name = 'register.html'
	form_class = UserCreationForm
	redirect_authenticated_user = True
	success_url = reverse_lazy('login')

	def form_valid(self, form):
		user = form.save()
		if user is not None:
			login(self.request, user)
		return super(RegisterPage, self).form_valid(form)

	def get(self, *args, **kwargs):
		if self.request.user.is_authenticated:
			return redirect('home')
		return super(RegisterPage, self).get(*args, **kwargs)

class SignupView(CreateView):
    form_class = UserCreationForm
    success_url = 'login'
    template_name = 'seller/register.html'

class LoginView(LoginView):
    form_class = AuthenticationForm
    redirect_authenticated_user = False
    success_url = '/buyer/home'
    template_name = 'seller/login.html'

def login_views(request):
# 	if request.method == 'POST':
# 		username = request.POST["username"]
# 		password = request.POST["password"]

# 		if username:
# 			if password:
# 				login_info = Seller.objects.filter(username=username)
# 				if login_info:
# 					user = username
# 					login(request, user)
# 					return render(request, 'buyer/home.html')

		
		# form = AuthenticationForm(data=request.POST)
		# if form.is_valid():
		# 	user = form.get_user()
			# log the user in
		
	# form = AuthenticationForm()
	# context = {'form': form}
	return render(request, 'seller/logins.html')

def logout_view(request):
    if request.method=='POST':
        logout(request)
        return redirect('home')


@login_required(login_url='/login') # This ensures user is login before he can access this page
def seller_create(request):
	form = CreateSeller()
	if request.method == 'POST':
		form = CreateSeller(request.POST, request.FILES)
		# if request.user.is_staff:
		# 	return HttpResponseForbidden(status=403)
		if form.is_valid():
			instance = form.save(commit=False) # This allows us to get & do something with the item b4 saving it
			instance.author = request.user # Helps to attach the currently login user as author of the article
			instance.save()
			#print(my_form.cleaned_data)
			# print(**my_form.cleaned_data)
			#Products_2.objects.create(**my_form.cleaned_data)
			messages.info(request, "Product Created Successfully.")
			return redirect('seller:home')
		messages.error(request, "Something went wrong with creating products.")
	context = {'form': form}
	return render(request, 'seller/create_product.html', context)


class SellerListView(View):
	def get(self, request, *args, **kwargs):
		#sellers = Seller.objects.all()
		sellers = Seller.objects.filter(author=request.user)
		context = {'sellers': sellers }
		print(request.user)
		return render(request, 'seller/seller_list.html', context)

def seller_detail(request, slug):
	#return HttpResponse(slug)
	seller = Seller.objects.get(slug=slug)
	context = {'seller': seller}
	return render(request, 'seller/seller_detail.html', context)
"""




