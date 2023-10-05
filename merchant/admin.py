from django.contrib import admin
from .models import Merchant, Merchant_Store, Products, Catagory, Product_Ratings, Orders

# Register your models here.

admin.site.register(Merchant)
admin.site.register(Merchant_Store)
admin.site.register(Products)
admin.site.register(Catagory)
admin.site.register(Product_Ratings)
admin.site.register(Orders)