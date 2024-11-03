from django.contrib.auth.views import LogoutView
from django.urls import path

from hotel_app import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("reservations/", views.user_reservations, name="reservations"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("hotels/", views.HotelListView.as_view(), name="hotels"),
    path("hotels/<int:hotel_id>/rooms/", views.hotel_rooms, name="hotel_rooms"),
]
