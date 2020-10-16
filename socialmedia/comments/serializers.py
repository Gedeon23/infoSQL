from rest_framework import serializers
from django.utils.timezone import now
from django.shortcuts import get_object_or_404
from .models import Comment
from Users.serializers import Profile_Serializer

class Comment_Serializer(serializers.ModelSerializer):
    author = Profile_Serializer(read_only=True)
    likes = serializers.SerializerMethodField()


    class Meta:
        model = Comment
        fields = '__all__'

    def get_likes(self, obj):
        return obj.likes.count()