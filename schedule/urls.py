from django.urls import path
from .views import *

app_name = "schedule"

urlpatterns = [
    path("create/", LessonCreateView.as_view(), name="create_lesson"),
    path("update/<pk>/", LessonUpdateView.as_view(), name="update_lesson"),
    path("delete/<pk>/", LessonDeleteView.as_view(), name="delete_lesson"),
    path("courses/", CourseView.as_view(), name="courses_list"),
    path("create/courses/", CourseCreateView.as_view(), name="create_course"),
    path("notifications/", NotificationView.as_view(), name="notifications_list"),
    path('send-email/', send_notification_view, name='send_email'),
]