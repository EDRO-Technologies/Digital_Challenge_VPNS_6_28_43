from django.shortcuts import render, redirect
from django.views.generic import FormView, TemplateView
from .forms import LoginForm
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile

class UserSignInView(FormView):
    template_name = "authorization.html"
    form_class = LoginForm
    success_url = reverse_lazy("main:main")

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("main:main")
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.get_user()
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "profile.html"
    login_url = "account:auth"

    def get_object(self):
        return Profile.objects.get(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        profile = Profile.objects.get(user=user)
        context["role"] = profile.role
        context["phone"] = profile.phone
        context["group"] = profile.group
        return context

def logout_view(request):
    logout(request)
    return redirect("account:auth")