#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.urls import path
from . import views


urlpatterns = [
    path(route="", view=views.index, name="index")
]
