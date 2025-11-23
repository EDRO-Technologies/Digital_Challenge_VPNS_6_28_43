from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    class Roles(models.TextChoices):
        STUDENT = "ST"
        TEACHER = "T"
        OTHER = "O"
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_name = models.CharField(name="last_name", max_length=75)
    name = models.CharField(name="name", max_length=75)
    surname = models.CharField(name="surname", max_length=75)
    phone = models.CharField(name="phone", max_length=20)
    group = models.CharField(name="group", max_length=15, null=True)
    role = models.CharField(name="role", choices=Roles, default=Roles.STUDENT)

    def __str__(self):
        return self.name

class Subjects(models.Model):
    title = models.CharField(name="title", max_length=150)

    def __str__(self):
        return self.title

class StudentsCourse(models.Model):
    title = models.CharField(name="title", max_length=30)
    participants = models.ForeignKey(Profile, on_delete=models.CASCADE)
    subjects = models.ForeignKey(Subjects, on_delete=models.CASCADE, null=True)
    institute = models.CharField(name="institute", max_length=10)

    def __str__(self):
        return self.title