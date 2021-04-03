from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.books, name='books'),
    path('register/', views.register, name='register'),
    path('login/', views.User_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    #возможно нужно добавить доп кнопку с addbook
    path('add_book/', views.add_book, name='add_book'),
    path('yourlib/', views.lib, name='yourlib')
]

urlpatterns += staticfiles_urlpatterns()