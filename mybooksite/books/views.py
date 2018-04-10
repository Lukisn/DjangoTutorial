from django.shortcuts import render
from .models import Author, Publisher, Book


def index(request):
    book = Book.objects.first()
    author = Author.objects.first()
    publisher = Publisher.objects.first()
    return render(request, "books_index.html", {
        "book": book,
        "author": author,
        "publisher": publisher,
    })


def list_authors(request):
    authors = Author.objects.all()
    return render(request, "list_authors.html", {"authors": authors})


def list_books(request):
    books = Book.objects.all()
    return render(request, "list_books.html", {"books": books})


def list_publishers(request):
    publishers = Publisher.objects.all()
    return render(request, "list_publishers.html", {"publishers": publishers})


def author_details(request, author_id):
    author = Author.objects.get(id=author_id)
    return render(request, "author_details.html", {"author": author})


def book_details(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, "book_details.html", {})


def publisher_details(request, publisher_id):
    publisher = Publisher.objects.get(id=publisher_id)
    return render(request, "publisher_details.html", {})
