from django import forms

from .models import Product

class CreateSeller(forms.ModelForm):

	class Meta:
		model = Product
		fields = [
			'name', 
	        'price',
	        'quantity',
	        'description',
			'slug',
			'thumb'
	    ]



