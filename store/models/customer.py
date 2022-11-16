from django.db import models

# Create your models here.
class Customer(models.Model):
    firstname=models.CharField(max_length=50, default="")
    lastname=models.CharField(max_length=50, default="")
    phone=models.CharField(max_length=15, default="")
    email = models.EmailField(max_length=25, default="" )
    password = models.CharField(max_length=15, default="")

    def register(self):
        self.save()
    
    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False
    
    def isExists(self):
        if Customer.objects.filter(email=self.email):
            return True
        return False