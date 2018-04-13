#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        label="Username",
        help_text="Enter your user name")
    password = forms.CharField(
        label="Password", widget=forms.PasswordInput,
        help_text="Enter your password")


class RegisterForm(forms.Form):
    username = forms.CharField(
        label="Username",
        help_text="Enter a unique username")
    email = forms.EmailField(
        label="Email",
        help_text="Enter an email address")
    password = forms.CharField(
        label="Password", widget=forms.PasswordInput,
        help_text="Enter a strong password")
    second_password = forms.CharField(
        label="Password again", widget=forms.PasswordInput,
        help_text="Enter the password again to avoid typos")

    def clean_username(self, min_chars=6):
        username = self.cleaned_data.get("username", "")
        num_chars = len(username)
        if num_chars < min_chars:
            msg = f"Not enough characters!" \
                  f"At least {min_chars} needed, but only {num_chars} given."
            raise forms.ValidationError(msg)
        other_users = User.objects.filter(username="username")
        if other_users:
            msg = "Username already used!"
            raise forms.ValidationError(msg)
        return username

    def clean_password(self, min_chars=6):
        password = self.cleaned_data.get("password", "")
        num_chars = len(password)
        if num_chars < min_chars:
            msg = f"Not enough characters!" \
                  f"At least {min_chars} needed, but only {num_chars} given."
            raise forms.ValidationError(msg)
        return password

    def clean_second_password(self):
        password = self.cleaned_data.get("password", "")
        second_password = self.cleaned_data.get("second_password", "")
        if password != second_password:
            print(password, second_password)
            msg = "Passwords don't match! Make sure that there are no typos."
            raise forms.ValidationError(msg)
        return second_password
