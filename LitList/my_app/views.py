from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def index(request):
  return render(request, 'index.html')

def details(request):
  return render(request, 'details.html')

def create(request):
  return render(request, 'create.html')

def update(request):
  return render(request, 'update.html')

def delete(request):
  return render(request, 'delete.html')