#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from django.urls import path
from .views import index, list_authors, list_books, list_publishers, \
    author_details, book_details, publisher_details


app_name = 'books'
urlpatterns = [
    path("", index, name="index"),
    path("author", list_authors, name="author_list"),
    path("author/<int:author_id>", author_details, name="author_details"),
    path("book", list_books, name="book_list"),
    path("book/<int:book_id>", book_details, name="book_details"),
    path("publisher", list_publishers, name="publisher_list"),
    path("publisher/<int:publisher_id>", publisher_details,
         name="publisher_details"),
]
