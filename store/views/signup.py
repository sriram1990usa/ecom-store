from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from store.models.customer import Customer
from django.views import View

class Signup(View):

    def get(self, request):
         return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        firstname = postData.get('firstname')
        lastname = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')        
        password = postData.get('password')

        value = {
            'firstname': firstname,
            'lastname': lastname,
            'phone': phone,
            'email': email
        }
        error_message = None

        customer = Customer(firstname=firstname,
                            lastname=lastname,
                            phone=phone,
                            email=email,
                            password=password)
        error_message = self.validateCustomer(customer)
        
        if not error_message:
            print(firstname, lastname, phone, email)
            customer.password = make_password(customer.password)
            customer.save()
            customer.register()

            return redirect('homepage')
        else:
            data = {
                'error': error_message,
                'values': value
            }
        return render(request, 'signup.html', data)       
   
    def validateCustomer(self, customer):
        error_message = None;
        if len(customer.firstname) < 4:
            error_message = "firstname must be >= 4 char"
        elif len(customer.lastname) < 4:
            error_message = "lastname must be <= 4 char"
        elif len(customer.phone) < 10:
            error_message = "phone num must be >=10 char"
        elif len(customer.email) < 4:
            error_message = "email must be >= 5 char"
        elif len(customer.password) < 4:
            error_message = "password must be >= 6 char"
        elif customer.isExists():
            error_message = "email exists"

        return error_message   
    