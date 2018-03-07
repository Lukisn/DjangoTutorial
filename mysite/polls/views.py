#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Polls Application Views."""
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.utils import timezone
from django.db.models import F

from .models import Question, Choice


# Function Views:
def index(request):
    """Index view function."""
    latest_question_list = Question.objects\
        .filter(pub_date__lte=timezone.now())\
        .order_by("-pub_date")[:5]
    return render(request, "polls/index.html", {
        "latest_question_list": latest_question_list,
    })


def detail(request, question_id):
    """Detail view function."""
    question = get_object_or_404(Question, pk=question_id)
    if question.pub_date <= timezone.now():
        return render(request, "polls/detail.html", {
            "question": question
        })
    raise Http404("This question is not yet published!")


def vote(request, question_id):
    """Vote view function."""
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html", {
            "question": question,
            "error_message": "You didn't select a choice!",
        })
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results",
                                            args=(question_id,)))


def results(request, question_id):
    """Results view function."""
    question = get_object_or_404(Question, pk=question_id)
    if question.pub_date <= timezone.now():
        return render(request, "polls/results.html", {"question": question})
    raise Http404("This question is not yet published!")
