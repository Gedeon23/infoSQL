from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from posts.models import Post
from Users.models import User_Profile
import datetime
from django.utils import timezone


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
