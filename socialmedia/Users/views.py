from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import User_Profile
from posts.models import Post



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/profile/')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def login(request):
    if request.method == 'POST':
        # form =     forms.py muss angelegt werden
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def logout(request):
    logout(request)
    return redirect('/')

def profile(request):
    User_Profile.objects.get(user = request.user)
    feed = Post.objects.filter(author = request.user).order_by('-date')
    return render(request, 'profile.html', {'request': request, 'feed': feed})
    
    # except:
    #     feed = Post.objects.all().order_by('-date')
    #     return render(request, 'home.html', {'user': request.user, 'profile': profile, 'feed': feed})