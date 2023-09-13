from django.contrib import admin
from .models import Merchant, Merchant_Store, Products

# Register your models here.

admin.site.register(Merchant)
admin.site.register(Merchant_Store)
admin.site.register(Products)