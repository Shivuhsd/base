from rest_framework import serializers
from .models import Merchant_Store, Products


class MyMerchart_Store(serializers.ModelSerializer):
    class Meta:
        model = Merchant_Store
        fields = '__all__'


class MyProducts(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'