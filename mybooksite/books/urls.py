#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from django.urls import path
from .views import index, list_authors, list_books, list_publishers, \
    author_details, book_details, publisher_details


urlpatterns = [
    path("", index),
    path("author", list_authors),
    path("author/<int:author_id>", author_details),
    path("book", list_books),
    path("book/<int:book_id>", book_details),
    path("publisher", list_publishers),
    path("publisher/<int:publisher_id>", publisher_details),
]
