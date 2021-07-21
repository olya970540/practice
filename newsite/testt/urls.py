from django.urls import path

from .views import *

urlpatterns = [
    path('', base, name='base'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('welcome/', welcome, name='welcome'),
]
