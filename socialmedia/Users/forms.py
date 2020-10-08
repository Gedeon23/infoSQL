from .models import User_Profile
from django import forms

class Profile_form(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('nickname', 'profile_pic', 'bio')
        widgets = {
          'bio': forms.Textarea(attrs={'rows':5, 'cols':40}),
        }