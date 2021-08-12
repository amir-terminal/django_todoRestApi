from django.db import models
from django.db.models import fields
from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from authentification.models import User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, max_length=128, min_length=6)

    class Meta:
        model = User
        fields = ("username", "email", "password")
        
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    

class LoginSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= User
        fields = ("email","password","token")
        ReadOnlyField = ('token')