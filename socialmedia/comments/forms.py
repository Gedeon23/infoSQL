from django import forms

class commentForm(forms.Form):
    content = forms.CharField(max_length=250)  

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].widget.attrs['placeholder'] = "enter your username"
        self.fields['content'].widget.attrs['class'] = 'form-control m-1'