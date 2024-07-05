from unicodedata import name
from django.urls import path
from . import views

urlpatterns = {
    path('', views.begin, name = 'beginner'),
    path('home', views.home, name = 'home'),
    path('book', views.book, name = 'book'),
    
    path('member', views.member, name = 'member'),
    path('member/login',views.member_login, name = 'member_login'),
    path('member/register', views.member_register, name = 'member_register'), 
    path('librarian', views.librarian, name = 'librarian')
}