from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from posts.models import Post


def home_view(request):

    feed = Post.objects.all()
    return render(request, 'home.html', {'request': request, 'feed': feed})
