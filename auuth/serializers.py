from rest_framework import serializers
from .models import Mymodel

class MymodelSerialization(serializers.ModelSerializer):
    class Meta:
        model = Mymodel
        fields = '__all__'