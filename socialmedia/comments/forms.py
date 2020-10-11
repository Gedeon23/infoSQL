from .models import Comment
from django import forms

class commentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('content', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].widget.attrs['placeholder'] = 'tell the world!'
        self.fields['content'].widget.attrs['class'] = 'form-control m-1'