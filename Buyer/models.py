from django.db import models
from django.contrib.auth.models import User
from merchant.models import Products

# Create your models here.

class UserExtention(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=12, blank=True)
    img = models.ImageField(blank=True, upload_to='user_photo/')
    gender = models.CharField(null=True, max_length=5)


    def __self__(self):
        return self.user
    
#A Model To Store Cart

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user.username + "----" + self.product_id.p_name


#A Model To Store History of User

class User_History(models.Model):
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    productid = models.ForeignKey(Products, on_delete=models.CASCADE)

    def __str__(self):
        return self.users.username 
    


#A Model To Store User/Buyer Address
class Address(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    mobile = models.IntegerField(null=True)
    pincode = models.IntegerField(null=True)
    address = models.TextField(null=True)
    town = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    landmark = models.CharField(max_length=100, null=True)
    alternate_phone = models.IntegerField(null=True)
    address_type = models.CharField(max_length=10, null=True)


    def __str__(self):
        return self.name + "----" + self.user_id.username



#A Model To Store Wishlist
class Wishlist(models.Model):
    u_id = models.ForeignKey(User, on_delete=models.CASCADE)
    p_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return self.u_id.username + "-----" + self.p_id.p_name