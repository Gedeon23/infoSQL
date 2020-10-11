from django.shortcuts import render, redirect, get_object_or_404
from .forms import Post_Creation_Form
from .models import Post
from comments.forms import commentForm

# Create your views here.
def post_Creation(request):
    if request.method == 'POST':
        form = Post_Creation_Form(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('/profile/')

    else:
        form = Post_Creation_Form()
        return render(request, 'post/create.html', {'form': form, 'request': request})

def delete_post(request, id):
    post = get_object_or_404(Post, pk=id)
    if post.author == request.user:
        post.delete()
        return redirect('/profile/')
    else: return redirect('/error/you_dont_have_permission/')

def post_view(request, id):
    if request.method == 'GET':
        post = get_object_or_404(Post, pk=id)
        form = commentForm()
        return render(request, 'post/detail.html', {
            'from': form, 
            'post': post
            })
    else:
        return redirect()