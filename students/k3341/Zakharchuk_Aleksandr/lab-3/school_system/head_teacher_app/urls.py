from django.urls import path
from head_teacher_app import views

urlpatterns = [
    path("rooms/", views.RoomListCreateAPIView.as_view(), name="room-list-create"),
    path("rooms/<int:pk>/", views.RoomDetailAPIView.as_view(), name="room-detail"),
]
