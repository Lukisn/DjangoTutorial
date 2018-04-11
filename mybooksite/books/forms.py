#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from django import forms
from .models import Publisher


TOPIC_CHOICES = (
    ("general", "General enquiry"),
    ("bug", "Bug report"),
    ("suggestion", "Suggestion"),
)


class ContactForm(forms.Form):
    topic = forms.ChoiceField(
        label="Topic", choices=TOPIC_CHOICES,
        help_text="Select the topic closest related to your feedback.")
    message = forms.CharField(
        label="Message", widget=forms.Textarea,
        help_text="Write your detailed feedback message here.")
    sender = forms.EmailField(
        label="Sender", required=False,
        help_text="Enter your email address here so we can come back to you. (optional)")

    def clean_message(self, min_words=10):
        message = self.cleaned_data.get("message", "")
        num_words = len(message.split())
        if num_words < min_words:
            msg = f"Not enough words!" \
                  f"At least {min_words} needed, but only {num_words} given"
            raise forms.ValidationError(msg)


class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ["name", "address", "city", "state_province", "country", "website"]
