from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.hashers import make_password, check_password
from django.views.decorators.csrf import csrf_protect
from .models import User, Product
from django.views import View
from django.http import HttpResponse
from django.http import HttpResponseForbidden
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

@csrf_protect
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


@csrf_protect
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


@csrf_protect
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




