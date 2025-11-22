from django.shortcuts import render
from django.views.generic import TemplateView
from account.models import Profile

class MainPageView(TemplateView):
    template_name = "main.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        role = Profile.objects.get(user=self.request.user).role
        context["role"] = role
        print(role)
        return context