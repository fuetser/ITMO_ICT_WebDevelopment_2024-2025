from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from head_teacher_app import models, serializers


class RoomListCreateAPIView(ListCreateAPIView):
    """
    Handles GET (list all rooms) and POST (create a new room).
    """
    queryset = models.Room.objects.all()
    serializer_class = serializers.RoomSerializer


class RoomDetailAPIView(RetrieveUpdateDestroyAPIView):
    """
    Handles GET, PUT, PATCH, and DELETE for a single room.
    """
    queryset = models.Room.objects.all()
    serializer_class = serializers.RoomSerializer


class TeacherListCreateAPIView(ListCreateAPIView):
    """
    Handles GET (list all teachers) and POST (create a new teacher).
    """
    queryset = models.Teacher.objects.all()
    serializer_class = serializers.TeacherSerializer


class TeacherDetailAPIView(RetrieveUpdateDestroyAPIView):
    """
    Handles GET, PUT, PATCH, and DELETE for a single teacher.
    """
    queryset = models.Teacher.objects.all()
    serializer_class = serializers.TeacherSerializer
