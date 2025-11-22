from django.db import models
from django.contrib.auth.models import User
from account.models import StudentsCourse

class Course(models.Model):
    title = models.TextField(name="course title")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(name="course description")

    def __str__(self):
        return title

class Lessons(models.Model):
    title = models.TextField(name="lesson title") 
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(name="lesson date")

class Notifications_lessons(models.Model):
    title = models.CharField(name="notififcation title", max_length=255)
    lesson_title = models.ForeignKey(Lessons, on_delete=models.SET_NULL, null=True)
    description = models.TextField(name="notification description")

class Notifications_courses(models.Model):
    title = models.CharField(name="notififcation title", max_length=255)
    course_title = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    description = models.TextField(name="notification description")

class StudyGroup(models.Model):
    participants = models.ManyToManyField(StudentsCourse)
    lessons = models.ForeignKey(Lessons, on_delete=models.CASCADE, name="lessons")

