from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Lessons
from account.models import Profile
from .forms import *

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
    form_class = CreateLesson
    template_name = "redact_lesson.html"
    context_object_name = "lesson"
    success_url = reverse_lazy('main:main')

def logout_view(request):
    logout(request)
    return redirect("account:auth")