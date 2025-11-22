from django.shortcuts import render
from django.views.generic import CreateView, FormView, TemplateView

class Zaglushka(TemplateView):
    template_name = "authorization.html"