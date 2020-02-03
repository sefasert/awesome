from django.urls import path

from denemem.views import index, users

app_name = 'denemem'

urlpatterns = [

    path('users/', users, name='users'),
    path('', index, name='index')


]
