from rest_framework import serializers

from head_teacher_app import models


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Room
        fields = "__all__"


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields = "__all__"


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Subject
        fields = "__all__"


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Class
        fields = ['class_id', 'class_name', 'homeroom_teacher_id']
        fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = "__all__"


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Schedule
        fields = "__all__"


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Grade
        fields = "__all__"
