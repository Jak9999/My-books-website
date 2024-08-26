from django.http import HttpResponse
from django.shortcuts import render
from .models import Books

print("books")


def index(request):
    books = Books.objects.all()  # Correctly fetches all books
    return render(request, 'index.html', {'books': books})  # Passes the books to the template
