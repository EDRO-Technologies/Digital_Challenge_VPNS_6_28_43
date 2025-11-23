from django import forms
from .models import Lessons, Courses
from datetime import timedelta

class CreateLesson(forms.ModelForm):
    class Meta:
        model = Lessons
        fields = ["title", 'date', 'duration', 'classroom', "flow"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "location__input"}),
            "date": forms.DateTimeInput(attrs={'type': 'datetime-local', "class": "location__input"}),
            "duration": forms.TextInput(attrs={"class": "location__input"}),
            "classroom": forms.TextInput(attrs={"class": "location__input"}),
            "flow": forms.TextInput(attrs={"class": "location__input"}),
        }
        labels = {
            "title": "Название",
            "date": "Дата и время проведения",
            "duration": "Длительность",
            "classroom": "Аудитория",
            "flow": "Группа"
        }

class RedactLesson(forms.ModelForm):
    class Meta:
        model = Lessons
        fields = ["title", 'date', 'duration', 'classroom', "flow", "comment"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "location__input"}),
            "date": forms.DateTimeInput(attrs={'type': 'datetime-local', "class": "location__input"}),
            "duration": forms.TextInput(attrs={"class": "location__input"}),
            "classroom": forms.TextInput(attrs={"class": "location__input"}),
            "flow": forms.TextInput(attrs={"class": "location__input"}),
            "comment": forms.Textarea()
        }
        labels = {
            "title": "Название",
            "date": "Дата и время проведения",
            "duration": "Длительность",
            "classroom": "Аудитория",
            "flow": "Группа",
            "comment": "Комментарий",
        }

class CreateCourse(forms.ModelForm):
    class Meta:
        model = Courses
        fields = ["title", "description"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "location__input"}),
            "description": forms.Textarea(attrs={"class": "location__input"}),
        }
        labels = {
            "title": "Название курса",
            "description": "Описание курса"
        }