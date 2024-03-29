from django.db import models
from django.contrib.auth.models import User


# Create your models here.


# customer table
class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank = True, on_delete = models.CASCADE)
    name = models.CharField(max_length= 200, null = True)
    email = models.CharField(max_length= 200,)
    def __str__(self):
        return self.name
    

# product table    
class Product(models.Model):
    name = models.CharField(max_length= 200, null = True)
    price = models.FloatField()
    digital = models.BooleanField(default= False, null=True, blank=False)
   
    def __str__(self):
        return self.name
    
 # order table   
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete = models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length = 200, null = True)
    
    
    def __str__(self):
        return str(self.id)
    # orderitem table
class OrderItem(models.Model):
    Product = models.ForeignKey(Product, on_delete = models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete = models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    
    # shipping table
class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete = models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length= 200, null = True)
    country = models.CharField(max_length= 200, null = True)
    city = models.CharField(max_length= 200, null = True)
    zipcode = models.CharField(max_length= 200, null = True)
    state = models.CharField(max_length= 200, null = True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return str(self.id)
    
    