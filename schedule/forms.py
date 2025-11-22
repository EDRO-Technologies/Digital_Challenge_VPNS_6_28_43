from django import forms
from .models import Lessons
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