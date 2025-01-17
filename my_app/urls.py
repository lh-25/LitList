from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('books/', views.book_index, name='book-index'),
  path('books/<int:book_id>/', views.book_details, name='book-detail'),
  path('books/create/', views.BookCreate.as_view(), name='book-create'),
  path('books/<int:pk>/update/', views.BookUpdate.as_view(), name='book-update'),
  path('books/<int:pk>/delete/', views.BookDelete.as_view(), name='book-delete'),
]