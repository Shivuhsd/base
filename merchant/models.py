from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Merchant_Store(models.Model):#A Model To Store Merchant Store Details
    owner = models.ForeignKey(User, on_delete=models.CASCADE)#foreign Key to User Object or Table
    m_name = models.CharField(max_length=200, blank=False)
    description = models.TextField()
    images = models.ImageField(upload_to='merchant_srote_images/', blank=True)
    videos = models.FileField(upload_to='merchant_store_videos/', blank=True)
    latitude = models.FloatField(max_length=10, blank=False, null=True)
    longitude = models.FloatField(max_length=10, blank=False, null=True)
    created_on = models.DateTimeField(auto_now_add=True, blank=True, null=True)


    def __str__(self):
        return self.m_name


#This Model Extends UserModel To Merchant Model
class Merchant(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    phone = models.IntegerField(null=True)
    ###Address We Can Link This Attribute to address table in buyer module

    def __str__(self):
        return self.phone
    


#A Model To Store Catogory of Product
class Catagory(models.Model):
    name = models.CharField(max_length=100, null=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name



class Products(models.Model):# A Model To Store Product Information
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE)
    store_id = models.ForeignKey(Merchant_Store, on_delete=models.CASCADE)
    p_catagory = models.ForeignKey(Catagory, on_delete=models.PROTECT, null=True)
    p_name = models.CharField(max_length=200, blank=False)
    price = models.FloatField(blank=False)
    product_description = models.TextField(blank=False)
    product_color = models.CharField(max_length=100, blank=True)
    product_specifications = models.TextField(blank=True)
    product_image = models.ImageField(upload_to='product_image/', null=True)
    product_videos = models.FileField(upload_to='product_videos/', null=True)
    created_on = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    availability = models.BooleanField(blank=False, default=True)



    def __str__(self):
        return self.p_name
    


class Product_Ratings(models.Model):# A Model To Store The Ratings
    p_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    ratings = models.IntegerField(blank=False)
    feedback = models.TextField(blank=True)
    rating_images = models.ImageField(upload_to='ratings_image/')
    rating_video = models.FileField(upload_to='rating_video/')
    created_on = models.DateTimeField(auto_now_add=True, blank=True)


    def __str__(self):
        return self.p_id.p_name + "----" + self.user_id.username
        

#Choices for Order Status
Order_Status = (
    ('placed', 'Placed'),
    ('shipped', 'Shipped'),
    ('outfordelivery', 'OutforDelivery'),
)


class Orders(models.Model):# A Model To Store Orders
    order_id = models.CharField(max_length=100, blank=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    p_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True, blank=True)
    status = models.CharField(max_length=20, choices=Order_Status, default=None)
    tracking_id = models.CharField(max_length=50, blank=False, default=None)


    def __str__(self):
        return self.order_id





    




    



    



    








  

