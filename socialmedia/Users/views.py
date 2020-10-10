from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from .models import User_Profile
from posts.models import Post
from .forms import loginForm, Profile_form


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
    return render(request, 'user/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            if (txen := request.GET.get('next')) is None:
                return redirect('/')
            else:
                return redirect(txen)
    else:
        form = loginForm()
    return render(request, 'user/login.html', {'form': form})


def logout_view(request):
    logout(request)
    print('next parameter: ', request.GET.get('next'))
    if (txen := request.GET.get('next')) is None:
        return redirect('/')
    else:
        return redirect(txen)

@login_required
def profile(request):
    try:
        User_Profile.objects.get(user=request.user)
        feed = Post.objects.filter(author=request.user).order_by('-date')
        return render(request, 'user/profile/overview.html', {'request': request, 'feed': feed})

    except:
        return redirect('/create_profile/')

@login_required
def profile_creation_view(request):
    if request.method == 'GET':
        form = Profile_form()
        return render(request, 'user/profile/create.html', {'form': form, 'request': request})
    else:
        form =Profile_form(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('/profile/')
