from django.urls import path

from project_first_app import views

urlpatterns = [
    path("owners/<int:owner_id>/", views.owner),
]
