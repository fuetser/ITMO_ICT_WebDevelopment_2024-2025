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


class SubjectListCreateAPIView(ListCreateAPIView):
    """
    Handles GET (list all subjects) and POST (create a new subject).
    """
    queryset = models.Subject.objects.all()
    serializer_class = serializers.SubjectSerializer


class SubjectDetailAPIView(RetrieveUpdateDestroyAPIView):
    """
    Handles GET, PUT, PATCH, and DELETE for a single subject.
    """
    queryset = models.Subject.objects.all()
    serializer_class = serializers.SubjectSerializer


class ClassListCreateAPIView(ListCreateAPIView):
    """
    Handles GET (list all classes) and POST (create a new class).
    """
    queryset = models.Class.objects.all()
    serializer_class = serializers.ClassSerializer


class ClassDetailAPIView(RetrieveUpdateDestroyAPIView):
    """
    Handles GET, PUT, PATCH, and DELETE for a single class.
    """
    queryset = models.Class.objects.all()
    serializer_class = serializers.ClassSerializer


class StudentListCreateAPIView(ListCreateAPIView):
    """
    Handles GET (list all students) and POST (create a new student).
    """
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer


class StudentDetailAPIView(RetrieveUpdateDestroyAPIView):
    """
    Handles GET, PUT, PATCH, and DELETE for a single student.
    """
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer


class ScheduleListCreateAPIView(ListCreateAPIView):
    """
    Handles GET (list all schedule records) and POST (create a new schedule record).
    """
    queryset = models.Schedule.objects.all()
    serializer_class = serializers.ScheduleSerializer


class ScheduleDetailAPIView(RetrieveUpdateDestroyAPIView):
    """
    Handles GET, PUT, PATCH, and DELETE for a single schedule record.
    """
    queryset = models.Schedule.objects.all()
    serializer_class = serializers.ScheduleSerializer


class GradeListCreateAPIView(ListCreateAPIView):
    """
    Handles GET (list all grades) and POST (create a new grade).
    """
    queryset = models.Grade.objects.all()
    serializer_class = serializers.GradeSerializer


class GradeDetailAPIView(RetrieveUpdateDestroyAPIView):
    """
    Handles GET, PUT, PATCH, and DELETE for a single grade.
    """
    queryset = models.Grade.objects.all()
    serializer_class = serializers.GradeSerializer
