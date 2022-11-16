from django.shortcuts import render , redirect
from django.contrib.auth.hashers import  check_password
from store.models.customer import Customer
from django.views import View
from store.models.product import Product

class Cart(View):
    def get(self , request):
        ids = list(request.session.get('cart').keys())
        print('line 10 views.cart: ', ids)
        products = Product.get_products_by_id(ids)
        print('line 11: ', products)
        return render(request , 'cart.html' , {'products' : products} )
                