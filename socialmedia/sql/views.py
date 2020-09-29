from django.shortcuts import render, redirect, get_object_or_404
from .forms import Sql_Form
from .models import Query

# Create your views here.
def sql(request):
    if request.method == 'POST':
        form = Sql_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin/sql')
    
    else:
        form = Sql_Form
    return render(request, 'sql.html', {'form': form})

def sql_query(request, id):
    query = get_object_or_404(Query, id=id)

    #content = Query.obj
    return render(request, 'sql_Abfrage.html', {query: query})