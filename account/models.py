from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    class Roles(models.TextChoices):
        STUDENT = "ST"
        TEACHER = "T"
        OTHER = "O"
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_name = models.CharField(name="last name", max_length=75)
    name = models.CharField(name="name", max_length=75)
    surname = models.CharField(name="surname", max_length=75)
    phone = models.CharField(name="phone", max_length=20)
    role = models.CharField(name="role", choices=Roles, default=Roles.STUDENT)

    def __str__(self):
        return self.name

class StudentsCourse(models.Model):
    title = models.CharField(name="student course title", max_length=30)
    participants = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    institute = models.CharField(name="institute", max_length=5)

    def __str__(self):
        return self.title
