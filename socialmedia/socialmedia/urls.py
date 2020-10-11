"""socialmedia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import auth_login
from django.urls import path
from Users.views import signup, login_view, logout_view, profile, profile_creation_view, edit_profile_view
from .views import home_view, discover, search
from sql.views import sql, sql_query
from django.conf.urls.static import static
from django.conf import settings
from posts.views import post_Creation, delete_post, post_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/sql', sql),
    path('admin/sql/<int:id>', sql_query),
    path('signup/', signup),
    path('', home_view),
    path('login/', login_view),
    path('profile/', profile),
    path('logout/', logout_view),
    path('user/', home_view),
    path('discover/', search),
    path('discover/<str:query>/', discover),
    path('create_post/', post_Creation),
    path('user/<int:id>/', home_view),
    path('user/<int:id>/comments/', home_view),
    path('user/<int:id>/posts/', home_view),
    path('create_profile/', profile_creation_view),
    path('edit_profile/', edit_profile_view),
    path('delete/post/<int:id>/', delete_post),
    path('post/<int:id>/', post_view)
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
