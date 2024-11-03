from django.urls import path

from hotel_app import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
]
