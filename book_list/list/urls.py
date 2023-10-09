from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_author/', views.add_author, name='add_author'),
    path('add_genre/', views.add_genre, name='add_genre'),
    path('book/create/', views.book_create, name='book_create'),
    path('book_list/', views.book_list, name='book_list'),
    path('book/<slug:slug>/', views.book_detail, name='book_detail'),
    path('book/<slug:slug>/update/', views.book_update, name='book_update'),
    path('book/<slug:slug>/delete/', views.book_delete, name='book_delete'),
]