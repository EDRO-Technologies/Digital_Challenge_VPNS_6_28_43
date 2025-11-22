from django.urls import path
from .views import *

app_name = "account"

urlpatterns = [
    path("auth/", Zaglushka.as_view(), name="auth"),
    path("profile/", Zaglushka2.as_view(), name="profile")

]