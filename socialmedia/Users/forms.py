from .models import User_Profile
from django import forms

class Profile_form(forms.ModelForm):

    class Meta:
        model = User_Profile
        fields = ('nickname', 'profile_pic', 'bio')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nickname'].widget.attrs['placeholder'] = "enter your nickname"
        self.fields['bio'].widget.attrs['placeholder'] = 'your bio'
        self.fields['profile_pic'].widget.attrs['placeholder'] = 'choose and profile picture'
        self.fields['nickname'].widget.attrs['class'] = 'form-control m-1'
        self.fields['bio'].widget.attrs['class'] = 'form-control m-1'
        self.fields['profile_pic'].widget.attrs['class'] = 'form-control m-1'

class loginForm(forms.Form):
    username = forms.CharField(label='username', max_length=100)
    password = forms.CharField(label='password', max_length=100)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = "enter your username"
        self.fields['password'].widget.attrs['placeholder'] = 'enter your password'
        self.fields['username'].widget.attrs['class'] = 'form-control m-1'
        self.fields['password'].widget.attrs['class'] = 'form-control m-1'
