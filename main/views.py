from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from account.models import Profile
from datetime import date, timedelta
from django.utils import timezone
from schedule.models import Lessons

class MainPageView(ListView):
    template_name = "main.html"
    model = Lessons
    context_object_name = 'lessons'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("account:auth")
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        role = Profile.objects.get(user=self.request.user).role
        lesson_date = Lessons.objects.all()

        lessons = []
        for i in lesson_date:
            lessons.append({
                "id": i.id,
                "year": str(i.date).split()[0],
                "title": i.title,
                "duration": i.duration,
                "classroom": i.classroom,
                "flow": i.flow,
                "comment": i.comment
                })

        today = timezone.now().date()
        week_start = today - timedelta(days=today.weekday())
        
        days_ru = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
        date = []
        for i, day in enumerate(days_ru):
            day_date = week_start + timedelta(days=i)
            date.append({
                "day": day,
                "date" : day_date,
                "date_str": day_date.strftime("%Y-%m-%d")
            })

        context["lessons"] = lessons
        context["role"] = role
        context["date"] = date

        return context

