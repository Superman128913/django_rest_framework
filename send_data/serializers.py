from dataclasses import fields
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from .models import *


#Serializer to Get user info
class UserSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='username')
    
    class Meta:
        model = User
        fields = ['id', 'name', 'email']


#Serializer to Get user detail
class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['available_funds', 'blocked_funds']


#Serializer to Register User
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.CharField(
    required=True,
    validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
    write_only=True, required=True, validators=[validate_password])
    class Meta:
        model = User
        fields = ('username', 'password', 'email')
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name='',
            last_name=''
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


#Serializer for sector
class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sectors
        fields = '__all__'


#Serializer for stock
class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stocks
        fields = ['name', 'sector', 'total_volume', 'unallocated', 'price']


#Serializer for stock
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'


#Serializer for ohlcv
class MarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Market_day
        fields = '__all__'


#Serializer for ohlcv
class OhlcvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ohlcv
        fields = '__all__'