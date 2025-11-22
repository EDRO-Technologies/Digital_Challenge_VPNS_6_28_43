from django.contrib import admin
from .models import *

admin.site.register(Courses)
admin.site.register(Lessons)
admin.site.register(Notifications_courses)
admin.site.register(Notifications_lessons)
admin.site.register(StudyGroup)