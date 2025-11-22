from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from account.models import Profile
from datetime import date
from django.utils import timezone


class MainPageView(TemplateView):
    template_name = "main.html"

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("account:auth")
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        role = Profile.objects.get(user=self.request.user).role
        tz = timezone.get_default_timezone()
        today_date = date.today()
        context["date"] = today_date
        context["role"] = role

        print(today_date)
        return context

