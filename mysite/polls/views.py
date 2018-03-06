#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Polls Application Views."""
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import Question, Choice


# Function Views:
def index(request):
    """Index view function."""
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    return render(request, "polls/index.html", {
        "latest_question_list": latest_question_list,
    })


def detail(request, question_id):
    """Detail view function."""
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {
        "question": question
    })


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
        selected_choice.votes += 1  # FIXME: race condition!
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question_id,)))


def results(request, question_id):
    """Results view function."""
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})


# Generic Class Views:
class IndexView(generic.ListView):
    """Index view class."""
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five questions."""
        return Question.objects\
            .filter(pub_date__lte=timezone.now())\
            .order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    """Detail view class."""
    model = Question
    template_name = "polls/detail.html"

    def get_queryset(self):
        """Return question details if published yet."""
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    """Results view class."""
    model = Question
    template_name = "polls/results.html"

    def get_queryset(self):
        """Return question results if published yet."""
        return Question.objects.filter(pub_date__lte=timezone.now())