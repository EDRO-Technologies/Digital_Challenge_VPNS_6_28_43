from django.urls import path
from .views import *

app_name = "main"

urlpatterns = [
    path("", MainPageView.as_view(), name="main")
]