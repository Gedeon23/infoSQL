from .models import Post
from django import forms

class Post_Creation_Form(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content', 'image')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder'] = "enter your post's title"
        self.fields['content'].widget.attrs['placeholder'] = 'tell the world!'
        self.fields['image'].widget.attrs['placeholder'] = 'choose and image'
        self.fields['title'].widget.attrs['class'] = 'form-control m-1'
        self.fields['content'].widget.attrs['class'] = 'form-control m-1'
        self.fields['image'].widget.attrs['class'] = 'form-control m-1'