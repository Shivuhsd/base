from rest_framework import generics
from .serializers import MymodelSerialization
from .models import Mymodel

# Create your views here.

class MymodelListView(generics.ListCreateAPIView):
    queryset = Mymodel.objects.all()
    serializer_class = MymodelSerialization