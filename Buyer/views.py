from django.shortcuts import render
from .models import Cart, User_History, UserExtention, Address
from .serializers import SerializedCart, SerializedUserExtention, SerializedUserHistory, SerializedAddress
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters, status
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework.response import Response

# Create your views here.

class CartView(ListAPIView):

    serializer_class = SerializedCart
    
    def get_queryset(self):
        user = self.kwargs.get('pk')

        queryset = Cart.objects.filter(user = user)

        return queryset



#Class View To Add To Cart
class AddCart(CreateAPIView):
    queryset = Cart
    serializer_class = SerializedCart


class UserView(RetrieveAPIView):
    queryset =UserExtention.objects.all()
    serializer_class = SerializedUserExtention


class UserHistoryView(ListAPIView):
    queryset = User_History.objects.all()
    serializer_class = SerializedUserHistory


class UserAddressView(CreateAPIView):
    serializer_class = SerializedAddress
   
    def perform_create(self, serializer):
        
        user_id = self.kwargs.get('pk')
        user = get_object_or_404(User, id=user_id)
        serializer.save(user_id = user)

    def post(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

        

