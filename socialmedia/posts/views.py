from django.shortcuts import render, redirect
from .forms import Post_Creation_Form

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
    