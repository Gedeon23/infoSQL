from rest_framework import serializers
from django.contrib.auth.models import User
from .models import User_Profile

class Profile_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User_Profile
        fields = '__all__'

class User_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'