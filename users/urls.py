
from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.create_user, name='create_user'),
]


trackpath/urls

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
]
