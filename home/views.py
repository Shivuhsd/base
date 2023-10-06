from merchant.models import Products
from merchant.serializers import MyProducts
from rest_framework.generics import ListAPIView
from rest_framework import filters

# Create your views here.

class ProductSearchView(ListAPIView):
    search_fields = ['p_name']
    filter_backends = (filters.SearchFilter,)
    queryset = Products.objects.all()
    serializer_class = MyProducts


#Class to list the Products

class ProductList(ListAPIView):
    queryset = Products.objects.all()
    serializer_class = MyProducts


