#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from django.shortcuts import render


def main(request):
    return render(request, "main.html")


def current_time(request):
    now = datetime.now()
    return render(request, "current_time.html", {"current_time": now})


def hours_ahead(request, offset):
    ahead = datetime.now() + timedelta(hours=offset)
    return render(request, "hours_ahead.html", {
        "offset": offset,
        "ahead_time": ahead
    })
