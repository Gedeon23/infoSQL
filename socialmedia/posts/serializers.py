from rest_framework import serializers
from Users.serializers import Profile_Serializer
from comments.serializers import Comment_Serializer
from .models import Post


class Post_Serializer(serializers.ModelSerializer):

    author = Profile_Serializer(read_only=True)
    likes = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = '__all__'

    def get_likes(self, obj):
        return obj.likes.count()


class Post_Detail_Serializer(serializers.ModelSerializer):

    author = Profile_Serializer(read_only=True)
    likes = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = '__all__'

    def get_likes(self, obj):
        return obj.likes.count()
