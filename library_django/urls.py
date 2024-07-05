from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.lobby, name = 'lobby'),
    path('home', views.home, name = 'home'),
    
]