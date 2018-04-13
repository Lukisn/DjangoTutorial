#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from django.shortcuts import render, redirect, reverse
from django.contrib import auth
from django.contrib.auth.models import User
from .forms import LoginForm, RegisterForm


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


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return redirect(reverse("main"))
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})


def logout(request):
    auth.logout(request)
    return redirect(reverse("main"))


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            new_user = User.objects.create_user(username=username, email=email, password=password)
            new_user.save()
            return redirect(reverse("login"))
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})
