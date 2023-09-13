from django.shortcuts import render
from .serializers import MyMerchart_Store, MyProducts
from .models import Merchant_Store, Products
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView



# Create your views here.

class MerchantStoreView(ListAPIView):
    queryset = Merchant_Store.objects.all()
    serializer_class = MyMerchart_Store


class MerchantStoreCreateView(CreateAPIView):
    queryset = Merchant_Store.objects.all()
    serializer_class = MyMerchart_Store

class MerchantStoreUpdate(UpdateAPIView):
    queryset = Merchant_Store.objects.all()
    serializer_class = MyMerchart_Store
    #lookup_field = 'pk'
