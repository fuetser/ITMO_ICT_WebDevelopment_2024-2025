from django import http
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_request
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import generic

from hotel_app import models


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


@login_required(login_url="/login/")
def user_reservations(request: http.HttpRequest) -> http.HttpResponse:
    reservations = models.Reservation.objects.filter(user_id=request.user)
    return render(request, "reservations.html", {"reservations": reservations})


def hotel_rooms(request: http.HttpRequest, hotel_id: int) -> http.HttpResponse:
    rooms = models.Room.objects.filter(hotel_id=hotel_id)
    return render(request, "rooms.html", {"rooms": rooms})


class HotelListView(generic.ListView):
    model = models.Hotel
    context_object_name = "hotels"
    template_name = "hotels.html"
