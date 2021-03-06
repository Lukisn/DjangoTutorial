#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from django.urls import path
from . import views


app_name = 'books'
urlpatterns = [
    path("", views.index, name="index"),

    path("author", views.list_authors, name="author_list"),
    path("author/<int:author_id>", views.author_details, name="author_details"),
    # TODO: implement add/edit pages for books

    path("book", views.list_books, name="book_list"),
    path("book/<int:book_id>", views.book_details, name="book_details"),
    # TODO: implement add/edit pages for authors

    path("publisher", views.list_publishers, name="publisher_list"),
    path("publisher/<int:publisher_id>", views.publisher_details,
         name="publisher_details"),
    path("publisher/add", views.add_publisher, name="add_publisher"),
    path("publisher/add/success", views.add_publisher_success, name="add_publisher_success"),
    path("publisher/edit/<int:publisher_id>", views.edit_publisher, name="edit_publisher"),
    path("publisher/edit/success", views.edit_publisher_success, name="edit_publisher_success"),
    # TODO: factor out generic views for listing, details, adding and editing

    path("search", views.search, name="search"),

    # TODO: move general contact page to project
    path("contact", views.contact, name="contact"),
    path("contact/thanks", views.contact_thanks, name="contact_thanks"),
]
