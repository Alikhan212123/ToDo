from rest_framework import serializers

from apps.todo.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ("id", "user", "title", "description", "image", "created_at")