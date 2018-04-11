#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from django.urls import path
import books.views as views


app_name = 'books'
urlpatterns = [
    path("", views.index, name="index"),
    path("author", views.list_authors, name="author_list"),
    path("author/<int:author_id>", views.author_details, name="author_details"),
    path("book", views.list_books, name="book_list"),
    path("book/<int:book_id>", views.book_details, name="book_details"),
    path("publisher", views.list_publishers, name="publisher_list"),
    path("publisher/<int:publisher_id>", views.publisher_details,
         name="publisher_details"),
    path("search", views.search, name="search"),
    path("contact", views.contact, name="contact"),
    path("contact/thanks", views.contact_thanks, name="contact_thanks"),
]
