from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('bookloan/list', views.display_bookloan, name = 'bookloan_list'), 
    path('bookloan/add', views.add_bookloan, name = 'add_bookloan'),
    path('bookloan/edit/<int:bookloan_id>', views.edit_bookloan, name = 'edit_bookloan'),
    path('bookloan/delete/<int:bookloan_id>', views.delete_bookloan, name = 'delete_bookloan')
]