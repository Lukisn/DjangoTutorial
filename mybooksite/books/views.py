from random import choice

from django.shortcuts import render, redirect, reverse
from django.db.models import Q
from django.core.mail import send_mail
from .models import Author, Publisher, Book
from .forms import ContactForm, PublisherForm


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
    # TODO: use get_object_or_404 shortcut
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


def search(request):
    query = request.GET.get("q", "").strip()
    results = []
    if query:
        qset = (  # create a complex query by "OR"ing the queries together:
            Q(title__contains=query) |
            Q(authors__first_name__contains=query) |
            Q(authors__last_name__contains=query)
        )
        results = Book.objects.filter(qset).distinct()
    return render(request, "books/search.html", {
        "query": query,
        "results": results,
    })


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            topic = form.cleaned_data["topic"]
            message = form.cleaned_data["message"]
            sender = form.cleaned_data.get("sender", "noreply@example.com")
            send_mail(
                subject=f"Feedback from your site, topic: {topic}",
                message=message,
                from_email=sender,
                recipient_list=["administrator@example.com"],
                fail_silently=True,
            )
            return redirect(reverse("books:contact_thanks"))
    else:
        form = ContactForm()
    return render(request, "books/contact.html", {"form": form})


def contact_thanks(request):
    return render(request, "books/contact_thanks.html")


def add_publisher(request):
    if request.method == "POST":
        form = PublisherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("books:add_publisher_success"))
    else:
        form = PublisherForm()
    return render(request, "books/add_publisher.html", {"form": form})


def add_publisher_success(request):
    return render(request, "books/add_publisher_success.html")


def edit_publisher(request, publisher_id):
    publisher = Publisher.objects.get(id=publisher_id)
    if request.method == "POST":
        form = PublisherForm(request.POST, instance=publisher)
        if form.is_valid():
            form.save()
            return redirect(reverse("books:edit_publisher_success"))
    else:
        form = PublisherForm(instance=publisher)
    return render(request, "books/edit_publisher.html", {"form": form})


def edit_publisher_success(request):
    return render(request, "books/edit_publisher_success.html")
