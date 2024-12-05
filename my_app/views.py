from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Book

# Create your views here.
# views.py



def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def book_index(request):
  books = Book.objects.all()
  return render(request, 'books/index.html', {'books': books})

def book_details(request, book_id):
  book = Book.objects.get(id=book_id)
  return render(request, 'books/details.html', {'book': book})

class BookCreate(CreateView):
  model = Book
  fields = '__all__'
  success_url = '/books/'

class BookUpdate(UpdateView):
    model = Book
    fields = '__all__'

class BookDelete(DeleteView):
    model = Book
    success_url = '/books/'

def delete(request):
  return render(request, 'delete.html')