from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from .forms import Sql_Form
from .models import Query
from django.contrib.auth.models import User

# Create your views here.

@staff_member_required
def sql(request):
    if request.user.is_staff:
        if request.method == 'POST':
            form = Sql_Form(request.POST)
            if form.is_valid():
                form.save()
                return redirect('admin/sql')

        else:
            form = Sql_Form

            query_list = Query.objects.all()

            return render(request, 'admin/sql.html', {'form': form, 'request': request, 'queries': query_list})
    else:
        return redirect('/')

@staff_member_required
def sql_query(request, id):
    query = get_object_or_404(Query, id=id)
    print(query)
    content = User.objects.raw('SELECT * FROM auth_user')
    return render(request, 'admin/sql_query.html', {'query': content})
