#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from django.http import HttpResponse
from django.shortcuts import render


def current_time(request):
    now = datetime.now()
    return render(request, "current_time.html", {"current_time": now})
    # response = f"<html><head></head><body><h3>Now</h3><p>{now}</p></body></html>"
    # return HttpResponse(response)


def hours_ahead(request, offset):
    ahead = datetime.now() + timedelta(hours=offset)
    return render(request, "hours_ahead.html", {
        "offset": offset,
        "ahead_time": ahead
    })
    # response = f"<html><head></head><body><h3>{offset} hours ahead</h3><p>{ahead}</p></body></html>"
    # return HttpResponse(response)
