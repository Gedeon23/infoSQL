from .models import Post
from django import forms

class Post_Creation_Form(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content', 'image')
        widgets = {
          'content': forms.Textarea(attrs={'rows':5, 'cols':40}),
        }