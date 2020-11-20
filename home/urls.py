from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.signupUser, name='signupUser'),
    path('login', views.loginUser, name='loginUser'),
    path('welcome', views.welcomeUser, name='welcomeUser')
]