#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.urls import path
from . import views


urlpatterns = [
    # e.g. /polls/
    path(route="", view=views.index, name="index"),
    # e.g. /polls/5/
    path(route="<int:question_id>/", view=views.detail, name="detail"),
    # e.g. /polls/5/results/
    path(route="<int:question_id>/results/", view=views.results, name="results"),
    # e.g. /polls/5/vote/
    path(route="<int:question_id>/vote/", view=views.vote, name="vote"),
]
