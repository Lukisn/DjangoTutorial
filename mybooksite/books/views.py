from random import choice

from django.shortcuts import render
from .models import Author, Publisher, Book


def index(request):
    book = choice(Book.objects.all())
    author = choice(Author.objects.all())
    publisher = choice(Publisher.objects.all())
    return render(request, "books/index.html", {
        "book": book,
        "author": author,
        "publisher": publisher,
    })


def list_authors(request):
    authors = Author.objects.all()
    return render(request, "books/list_authors.html", {"authors": authors})


def list_books(request):
    books = Book.objects.all()
    return render(request, "books/list_books.html", {"books": books})


def list_publishers(request):
    publishers = Publisher.objects.all()
    return render(request, "books/list_publishers.html", {
        "publishers": publishers
    })


def author_details(request, author_id):
    author = Author.objects.get(id=author_id)
    return render(request, "books/details_author.html", {"author": author})


def book_details(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, "books/details_book.html", {"book": book})


def publisher_details(request, publisher_id):
    publisher = Publisher.objects.get(id=publisher_id)
    return render(request, "books/details_publisher.html", {
        "publisher": publisher
    })
