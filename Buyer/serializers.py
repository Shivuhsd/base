from rest_framework import serializers
from . models import Cart, User_History, UserExtention


#Cart
class SerializedCart(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fileds = '__all__'


#userExtension

class SerializedUserExtention(serializers.ModelSerializer):
    class Meta:
        model = UserExtention
        fields = '__all__'


#UserHistory

class SerializedUserHistory(serializers.ModelSerializer):
    class Meta:
        model = User_History
        fields = '__all__'