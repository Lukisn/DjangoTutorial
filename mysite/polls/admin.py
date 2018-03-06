#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Admin interface configuration."""
from django.contrib.admin import ModelAdmin, TabularInline, site
from .models import Question, Choice


class ChoiceInline(TabularInline):
    model = Choice
    extra = 1


class QuestionAdmin(ModelAdmin):
    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"],
                              "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]


site.register(Question, QuestionAdmin)
