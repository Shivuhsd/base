from rest_framework import serializers
from .models import Merchant_Store, Products, Product_Ratings, Merchant, Orders, Catagory


class MyMerchart_Store(serializers.ModelSerializer):
    class Meta:
        model = Merchant_Store
        fields = '__all__'


class MyProducts(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'


class MyCatagory(serializers.ModelSerializer):
    class Meta:
        model = Catagory
        fields = '__all__'
