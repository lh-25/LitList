from django.shortcuts import render

# Create your views here.
# views.py

class Book:
    def __init__(self, title, author, published_date, genre, status, description):
        self.title = title
        self.author = author
        self.published_date = published_date
        self.genre = genre
        self.status = status
        self.description = description

# Create a list of Book instances
books = [
    Book(
        'The Great Gatsby', 
        'F. Scott Fitzgerald', 
        '1925-04-10', 
        'Fiction', 
        'finished', 
        'A tragic story of Jay Gatsby and his unrequited love for Daisy Buchanan.'
    ),
    Book(
        '1984', 
        'George Orwell', 
        '1949-06-08', 
        'Dystopian', 
        'not_started', 
        'A chilling dystopian novel about totalitarianism and surveillance.'
    ),
    Book(
        'To Kill a Mockingbird', 
        'Harper Lee', 
        '1960-07-11', 
        'Classic', 
        'reading', 
        'A powerful tale of racial injustice and childhood in the Deep South.'
    ),
    Book(
        'Brave New World', 
        'Aldous Huxley', 
        '1932-08-30', 
        'Science Fiction', 
        'finished', 
        'A futuristic world dominated by technology, conditioning, and hedonism.'
    ),
]


def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def book_index(request):
  return render(request, 'books/index.html', {'books': books})

def details(request):
  return render(request, 'details.html')

def create(request):
  return render(request, 'create.html')

def update(request):
  return render(request, 'update.html')

def delete(request):
  return render(request, 'delete.html')