from rest_framework import serializers
from .models import Job, Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['coin', 'output', 'created_at']

class JobSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = Job
        fields = ['id', 'tasks', 'created_at']
