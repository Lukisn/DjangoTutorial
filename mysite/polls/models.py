#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Polls Application Models."""
from datetime import timedelta
from django.db.models import Model, CharField, DateTimeField, ForeignKey, \
    IntegerField, CASCADE
from django.utils import timezone


class Question(Model):
    question_text = CharField(max_length=200)
    pub_date = DateTimeField("publishing date")

    def __str__(self):
        return f"{self.question_text}"

    def was_published_recently(self):
        now = timezone.now()
        a_day_ago = now - timedelta(days=1)
        return a_day_ago <= self.pub_date <= now

    was_published_recently.short_description = "Published recently?"
    was_published_recently.admin_order_field = "pub_date"
    was_published_recently.boolean = True


class Choice(Model):
    question = ForeignKey(Question, on_delete=CASCADE)
    choice_text = CharField(max_length=200)
    votes = IntegerField(default=0)

    def __str__(self):
        return f"{self.choice_text}"
