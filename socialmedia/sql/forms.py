from .models import Query
from django.forms import ModelForm

class Sql_Form(ModelForm):
    class Meta:
        model = Query
        fields = ['title', 'table', 'query']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder'] = 'enter full title'
        self.fields['table'].widget.attrs['placeholder'] = 'choose table'
        self.fields['query'].widget.attrs['placeholder'] = 'write your query here'
        self.fields['title'].widget.attrs['class'] = 'form-control m-1'
        self.fields['table'].widget.attrs['class'] = 'form-control m-1'
        self.fields['query'].widget.attrs['class'] = 'form-control m-1'