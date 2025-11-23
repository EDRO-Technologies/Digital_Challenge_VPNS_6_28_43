from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, TemplateView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.http import HttpResponse
from .models import Lessons, Courses
from account.models import Profile
from .forms import *

def send_notification_view(request):
    # Получаем данные из запроса или из других источников
    user_email = 'ilya.surgutskij11@gmail.com'

    send_mail(
        'Важное уведомление',
        'Здравствуйте! У вас новое уведомление на сайте.',
        'hooloit147@list.ru',
        [user_email],
        fail_silently=False,
    )

    return HttpResponse('Уведомление отправлено!')

class LessonCreateView(CreateView):
    model = Lessons
    form_class = CreateLesson
    template_name = "create_lesson.html"
    success_url = reverse_lazy("schedule:create_lesson")

    def form_valid(self, form):
        form.instance.owner = Profile.objects.get(user=self.request.user)
        return super().form_valid(form)

class LessonUpdateView(UpdateView):
    model = Lessons
    form_class = RedactLesson
    template_name = "redact_lesson.html"
    context_object_name = "lesson"
    success_url = reverse_lazy('main:main')

    def form_valid(self, form):
        lesson = form.save(commit=False)

        title = form.cleaned_data.get('title')
        owner = form.cleaned_data.get('owner')
        date = form.cleaned_data.get('date')
        duration = form.cleaned_data.get('duration')
        classroom = form.cleaned_data.get('classroom')
        flow = form.cleaned_data.get('flow')
        comment = form.cleaned_data.get('comment')

        print(title,owner,date,duration,classroom,flow,comment)
        print("\n",f"Заголовок: {title}")
        print(f"Описание: {comment}")
        print(f"Дата: {date}")

        user_email = 'hooloit147@gmail.com'

        send_mail(
            f"""{comment}{title}{owner}{date}{duration}{classroom}{flow}""",
            f"""{comment}
                        {title}
                        {owner}
                        {date}
                        {duration}
                        {classroom}
                        {flow}
                        """,
            'hooloit147@list.ru',
            [user_email],
            fail_silently=False,
        )

        lesson.save()
        
        return super().form_valid(form)

class LessonDeleteView(DeleteView):
    model = Lessons
    template_name = "delete_lesson.html"
    success_url = reverse_lazy("main:main")

class CourseCreateView(CreateView):
    model = Courses
    template_name = "create_course.html"
    form_class = CreateCourse
    success_url = reverse_lazy("schedule:create_course")

    def form_valid(self, form):
        form.instance.owner = Profile.objects.get(user=self.request.user)
        return super().form_valid(form)

class CourseView(ListView):
    template_name = "courses.html"
    model = Courses
    context_object_name = "courses"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.get(user=self.request.user)
        context["name"] = profile.name
        context["last_name"] = profile.last_name
        context["surname"] = profile.surname
        return context

class NotificationView(TemplateView):
    template_name = "notifications.html"
    
def logout_view(request):
    logout(request)
    return redirect("account:auth")