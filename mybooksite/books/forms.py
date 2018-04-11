#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from django import forms


TOPIC_CHOICES = (
    ("general", "General enquiry"),
    ("bug", "Bug report"),
    ("suggestion", "Suggestion"),
)


class ContactForm(forms.Form):
    topic = forms.ChoiceField(choices=TOPIC_CHOICES)
    message = forms.CharField(widget=forms.Textarea())
    sender = forms.EmailField(required=False)

    def clean_message(self, min_words=10):
        message = self.cleaned_data.get("message", "")
        num_words = len(message.split())
        if num_words < min_words:
            msg = f"Not enough words!" \
                  f"At least {min_words} needed, but only {num_words} given"
            raise forms.ValidationError(msg)
