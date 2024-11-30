from django.db.models import Avg, Count
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

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


class ScheduleByClassAPIView(APIView):
    """
    Handles GET for a single schedule record
    """

    def get(self, request, *args, **kwargs):
        class_id = request.query_params.get("class_id")
        day_of_week = request.query_params.get("day_of_week")
        lesson_number = request.query_params.get("lesson_number")

        if not class_id or not day_of_week or not lesson_number:
            return Response(
                {"error": "The class_id, day_of_week and lesson_number parameters are required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        schedule_record = models.Schedule.objects.filter(
            student_class__id=class_id,
            day_of_week=day_of_week,
            lesson_number=lesson_number
        ).first()

        if not schedule_record:
            return Response(
                {"message": "No schedule record found for given parameters"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = serializers.ScheduleSerializer(schedule_record)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TeachersPerSubjectAPIView(APIView):
    """
    Handles GET info about teachers for each subject
    """

    def get(self, request, *args, **kwargs):
        data = (
            models.Schedule.objects.values("subject")
            .annotate(teacher_count=Count("teacher", distinct=True))
            .order_by("subject")
        )

        result = []
        for entry in data:
            subject = models.Subject.objects.filter(id=entry["subject"]).first()
            result.append({
                "subject_id": entry["subject"],
                "subject_name": subject.name if subject else "Unknown",
                "teacher_count": entry["teacher_count"]
            })

        return Response(result, status=status.HTTP_200_OK)


class GenderCountPerClassAPIView(APIView):
    """
    Handles GET the number of boys and girls in each class
    """

    def get(self, request, *args, **kwargs):
        gender_counts = (
            models.Student.objects.values("student_class", "gender")
            .annotate(count=Count("id"))
            .order_by("student_class", "gender")
        )

        result = {}
        for entry in gender_counts:
            class_id = entry["student_class"]
            gender = entry["gender"]
            count = entry["count"]

            if class_id not in result:
                result[class_id] = {"boys": 0, "girls": 0}

            # Добавление данных о поле
            if gender == "M":
                result[class_id]["boys"] = count
            else:
                result[class_id]["girls"] = count

        formatted_result = []

        for class_id, counts in result.items():
            class_obj = models.Class.objects.filter(id=class_id).first()
            formatted_result.append({
                "class_id": class_id,
                "class_name": class_obj.class_name if class_obj else "Unknown",
                "boys": counts["boys"],
                "girls": counts["girls"]
            })

        return Response(formatted_result, status=status.HTTP_200_OK)


class RoomCountAPIView(APIView):
    """
    Handles GET the number of basic and specialized rooms
    """

    def get(self, request, *args, **kwargs):
        room_counts = (
            models.Room.objects.values("is_specialized")
            .annotate(count=Count("room_number"))
        )

        result = {
            "basic_rooms": 0,
            "specialized_rooms": 0
        }

        for entry in room_counts:
            if entry["is_specialized"]:
                result["specialized_rooms"] = entry["count"]
            else:
                result["basic_rooms"] = entry["count"]

        return Response(result, status=status.HTTP_200_OK)


class ClassPerformanceReportAPIView(APIView):
    """
    Handles GET info about class performance
    """

    def get(self, request, *args, **kwargs):
        class_id = request.query_params.get("class_id")
        quarter_number = request.query_params.get("quarter_number")
        if not class_id or not quarter_number:
            return Response(
                {"error": "The class_id and quarter_number parameters are required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        class_obj = models.Class.objects.filter(id=class_id).first()
        if not class_obj:
            return Response(
                {"error": f"Class with id {class_id} not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        grades = (
            models.Grade.objects.filter(student__student_class__id=class_id, quarter=quarter_number)
            .values("subject")
            .annotate(
                average_grade=Avg("grade"),
                total_students=Count("student", distinct=True)
            )
        )

        subjects_report = []
        for grade in grades:
            subject = models.Subject.objects.filter(id=grade["subject"]).first()
            subjects_report.append({
                "subject_id": grade["subject"],
                "subject_name": subject.name if subject else "Unknown",
                "average_grade": round(grade["average_grade"], 2),
                "total_students": grade["total_students"]
            })

        class_average_grade = (
            models.Grade.objects.filter(student__student_class__id=class_id, quarter=quarter_number)
            .aggregate(average_class_grade=Avg("grade"))
            .get("average_class_grade")
        )

        homeroom_teacher = class_obj.homeroom_teacher
        teacher_info = {
            "teacher_id": homeroom_teacher.id,
            "first_name": homeroom_teacher.first_name,
            "last_name": homeroom_teacher.last_name,
            "patronymic": homeroom_teacher.patronymic
        } if homeroom_teacher else None

        total_students = models.Student.objects.filter(student_class__id=class_id).count()

        report = {
            "class_id": class_id,
            "class_name": class_obj.class_name,
            "homeroom_teacher": teacher_info,
            "total_students": total_students,
            "average_class_grade": round(class_average_grade, 2) if class_average_grade else None,
            "subjects_report": subjects_report
        }

        return Response(report, status=status.HTTP_200_OK)
