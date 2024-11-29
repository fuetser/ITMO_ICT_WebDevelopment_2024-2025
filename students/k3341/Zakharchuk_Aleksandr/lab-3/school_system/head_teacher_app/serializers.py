from rest_framework import serializers

from head_teacher_app import models


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Room
        fields = "__all__"
