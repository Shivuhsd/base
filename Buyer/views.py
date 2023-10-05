from django.shortcuts import render
from .models import Cart, User_History, UserExtention
from .serializers import SerializedCart, SerializedUserExtention, SerializedUserHistory
from rest_framework.generics import ListAPIView, RetrieveAPIView

# Create your views here.

class CartView(ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = SerializedCart


class UserView(RetrieveAPIView):
    queryset =UserExtention.objects.all()
    serializer_class = SerializedUserExtention
    lookup_field = 'pk'


class UserHistoryView(ListAPIView):
    queryset = User_History.objects.all()
    serializer_class = SerializedUserHistory

