from django.db import models
from django.utils.crypto import get_random_string
import datetime

# Create your models here.

ORDER_STATUS_CHOICES= (
    ('Not Yet Shipped','Not Yet Shipped'),
    ('Order Shipped','Order Shipped'),
    ('Refunded','Refunded'),
    ('Cancelled','Cancelled'),
    ('Delivery Booked','Delivery Booked')
)

class User(models.Model):
    full_name = models.CharField(max_length=20)
    email =  models.EmailField()
    password = models.CharField(max_length=20)

    def __str__(self):
        content = str(self.pk) +' '+ self.full_name
        return content
  

# class Location_detail(models.Model):
#     order_id = models.CharField(max_length=50)
#     customer_name = models.CharField(max_length=20)
#     status = models.CharField(default='Not Yet Shipped',choices=ORDER_STATUS_CHOICES, max_length=50)
#     location = models.TextField(default='Not Yet Shipped')
#     date = models.TextField()

#     def __str__(self):
#         return (self.customer_name + self.order_id)

class New_order(models.Model):
    
    def generate_random_id():
        return get_random_string(10,allowed_chars='0123456789ABCDEFGHI')
   
   
    name = models.CharField(max_length=20)
    contact = models.CharField(max_length=12)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    source = models.CharField(max_length=500)
    destination = models.CharField(max_length=500)
    weight = models.CharField(default = '0.00',max_length=6)
    cost = models.CharField(default='0.00',max_length=10)
    id= models.CharField(default= generate_random_id(),max_length=15,primary_key=True)
    ordered_date = models.CharField(default = " ",max_length=100)
    status = models.CharField(default='Delivery Booked',choices=ORDER_STATUS_CHOICES, max_length=50)
    location = models.TextField(default='Not Yet Shipped')
    shipment_date = models.TextField(default = "",null=True,blank=True)
    
    
    def __str__(self):
        return (self.id + ' ' + self.name)
