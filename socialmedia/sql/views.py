from django.shortcuts import render, redirect, get_object_or_404
from .forms import Sql_Form
from .models import Query
from django.contrib.auth.models import User

# Create your views here.


def sql(request):
    if request.method == 'POST':
        form = Sql_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin/sql')

    else:
        form = Sql_Form

    current_User = request.user

    if current_User.is_staff:
        return render(request, 'sql.html', {'form': form, 'user': current_User})
    else:
        return redirect('')


def sql_query(request, id):
    query = get_object_or_404(Query, id=id)
    print(query)
    content = User.objects.raw('SELECT * FROM auth_user')
    return render(request, 'sql_query.html', {'query': content})
