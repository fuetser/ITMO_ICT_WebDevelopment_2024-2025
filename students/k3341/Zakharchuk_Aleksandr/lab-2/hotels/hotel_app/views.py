from django import http
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as login_request
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.urls import reverse


def register(request: http.HttpRequest) -> http.HttpResponse:
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("login"))
    else:
        form = UserCreationForm()

    return render(request, "register.html", {"form": form})


def login(request: http.HttpRequest) -> http.HttpResponse:
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)

        if user is not None:
            login_request(request, user)
            return redirect("/reservations/")

        return redirect(reverse("login"))

    return render(request, "login.html")
