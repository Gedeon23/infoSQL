from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from posts.models import Post
from posts.serializers import Post_Serializer
from Users.models import User_Profile
import datetime
from django.utils import timezone
from django.apps import apps


def home_view(request):

    feed = Post.objects.all().order_by('-date')
    return render(request, 'home.html', {'request': request, 'feed': feed})


def search(request):
    return render(request, 'search/bar.html', {'request': request})


def discover(request, query):

    posts = Post.objects.filter(content__contains=query).order_by('-date')[:5]
    users = User.objects.filter(
        username__contains=query).order_by('-date_joined')[:5]
    return render(request, 'search/results.html', {'request': request, 'feed': {'posts': posts, 'users': users}})

def error(request, code):
    return render(request, 'error.html', {'code': code})

def feed_view(request):
    return render(request, 'feed.html', {})

class Api_Serve_Feed_Posts(APIView):
    def post(self, request):
        loadedPosts = []
        loadedPost = self.request.POST.get('loadedPosts')
        posts = Post.objects.filter(author__followers=self.request.user).order_by('-date').exclude(pk__in=loadedPosts)[:25]
        serialized = Post_Serializer(posts, many=True)
        data = {
            'posts': serialized.data
        }
        return Response(data)
