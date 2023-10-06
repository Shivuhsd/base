from rest_framework import serializers
from . models import Cart, User_History, UserExtention, Address


#Cart
class SerializedCart(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['product_id', 'user']


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


#Address

class SerializedAddress(serializers.ModelSerializer):
    class Meta:
        model = Address
        exclude = ['user_id']

