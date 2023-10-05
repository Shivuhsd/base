from django.contrib import admin
from .models import Cart, UserExtention, User_History, Address, Wishlist

# Register your models here.
admin.site.register(Cart)
admin.site.register(UserExtention)
admin.site.register(User_History)
admin.site.register(Address)
admin.site.register(Wishlist)