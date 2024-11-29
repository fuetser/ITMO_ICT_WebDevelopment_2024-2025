from django.db import models

GENDER_CHOICES = [("M", "Male"), ("F", "Female")]


class Room(models.Model):
    room_number = models.IntegerField(primary_key=True)
    is_specialized = models.BooleanField(default=False)


class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    assigned_room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)
    is_homeroom_teacher = models.BooleanField(default=False)


class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True)


class Class(models.Model):
    class_name = models.CharField(max_length=20, unique=True)
    homeroom_teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE)


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    student_class = models.ForeignKey(Class, on_delete=models.CASCADE)


class Schedule(models.Model):
    DAYS_OF_WEEK = [
        ("Monday", "Monday"),
        ("Tuesday", "Tuesday"),
        ("Wednesday", "Wednesday"),
        ("Thursday", "Thursday"),
        ("Friday", "Friday"),
        ("Saturday", "Saturday"),
        ("Sunday", "Sunday"),
    ]

    student_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    room_number = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)
    day_of_week = models.CharField(max_length=10, choices=DAYS_OF_WEEK)
    lesson_number = models.IntegerField()

    class Meta:
        unique_together = ("student_class", "subject", "day_of_week", "lesson_number")


class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    quarter = models.IntegerField()
    grade = models.IntegerField()
    is_final = models.BooleanField(default=False)
