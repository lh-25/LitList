from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('home/', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('books/', views.book_index, name='book-index'),
  path('details/', views.details, name='details'),
  path('create/', views.create, name='create'),
  path('update/', views.update, name='update'),
  path('delete/', views.delete, name='delete'),
]