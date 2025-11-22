from django.shortcuts import render
from django.views.generic import CreateView, FormView, TemplateView
from .forms import LoginForm
from django.urls import reverse_lazy

# class Zaglushka(TemplateView):
#     template_name = "authorization.html"
    
# class Zaglushka2(TemplateView):
#     template_name = "profile.html"

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