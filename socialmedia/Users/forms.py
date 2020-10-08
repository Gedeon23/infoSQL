from .models import User_Profile
from django import forms

class Profile_form(forms.ModelForm):

    class Meta:
        model = User_Profile
        fields = ('nickname', 'profile_pic', 'bio')
        widgets = {
          'bio': forms.Textarea(attrs={'rows':5, 'cols':40}),
        }

class loginForm(forms.Form):
    username = forms.CharField(label='username', max_length=100)
    password = forms.CharField(label='password', max_length=100)