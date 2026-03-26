from rest_framework import serializers
from .models import TaskAndDeadlinePlanner

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskAndDeadlinePlanner
        fields = '__all__'

