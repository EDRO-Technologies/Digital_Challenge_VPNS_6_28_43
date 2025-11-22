from django.urls import path
from .views import *

app_name = "schedule"

urlpatterns = [
    path("create/", LessonCreateView.as_view(), name="create_lesson"),
    path("update/<pk>/", LessonUpdateView.as_view(), name="update_lesson")
]