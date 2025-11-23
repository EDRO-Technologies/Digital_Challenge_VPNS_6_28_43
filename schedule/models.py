from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from account.models import Profile, StudentsCourse

class Courses(models.Model):
    title = models.TextField(name="title")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(name="description")

    def __str__(self):
        return self.title

class Lessons(models.Model):
    title = models.TextField(name="title") 
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date = models.DateTimeField(name="date", default=timezone.now)
    duration = models.CharField(name="duration", max_length=100, blank=True)
    classroom = models.CharField(name="classroom", max_length=15, blank=True)
    flow = models.CharField(name="flow", max_length=150, blank=True)
    comment = models.TextField(name="comment", blank=True)

    def get_day_of_week(self):
        return self.date.strftime('%A')

class Notifications_lessons(models.Model):
    title = models.CharField(name="title", max_length=255)
    lesson_title = models.ForeignKey(Lessons, on_delete=models.SET_NULL, null=True)
    description = models.TextField(name="description")

class Notifications_courses(models.Model):
    title = models.CharField(name="title", max_length=255)
    course_title = models.ForeignKey(Courses, on_delete=models.SET_NULL, null=True)
    description = models.TextField(name="notification description")

class StudyGroup(models.Model):
    participants = models.ManyToManyField(StudentsCourse)
    lessons = models.ForeignKey(Lessons, on_delete=models.CASCADE, name="lessons")

