from django.urls import path
from .views import *

app_name = "account"

urlpatterns = [
    path("auth/", UserSignInView.as_view(), name="auth"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("logout/", logout_view, name="logout"),
]