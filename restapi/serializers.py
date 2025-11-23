from rest_framework import serializers
from schedule.models import *


class LessonsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lessons
        fields = '__all__'

