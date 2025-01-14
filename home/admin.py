from django.contrib import admin
from . models import UserQuery, UserComment

# Register your models here.

admin.site.register(UserQuery)
admin.site.register(UserComment)