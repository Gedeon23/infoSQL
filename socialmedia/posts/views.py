from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import Post_Serializer
from .forms import Post_Creation_Form
from .models import Post
from comments.forms import commentForm

class Get_Post_List(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serialized = Post_Serializer(posts, many=True)
        return Response(serialized.data)

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

def edit_post_view(request, id):
    post = get_object_or_404(Post, pk=id)
    if post.author == request.user:
        if request.method == 'POST':
            form = Post_Creation_Form(request.POST, request.FILES, instance=post)
            if form.is_valid():
                form.save()
                return redirect('/post/' + str(id) + '/')

        else:
            form = Post_Creation_Form(instance=post)
            return render(request, 'post/edit.html', {'form': form, 'request': request})
    else: return redirect('/error/you can only edit your own posts/')


def delete_post(request, id):
    post = get_object_or_404(Post, pk=id)
    if post.author == request.user:
        post.delete()
        return redirect('/profile/')
    else: return redirect('/error/you can only delete your own posts/')

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


class Post_Like_API(APIView):
    def get(self, request, id):
        post = get_object_or_404(Post, pk=id)
        user = self.request.user
        if user in post.likes.all():
            liked = False
            post.likes.remove(user)
        else:
            liked = True
            post.likes.add(user)
            
        like_count = post.likes.count()
        data = {
            'updated': True,
            'liked': liked,
            'like_count': like_count
        }
        return Response(data)