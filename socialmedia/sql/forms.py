from .models import Query
from django.forms import ModelForm

class Sql_Form(ModelForm):
    class Meta:
        model = Query
        fields = ['title', 'query']