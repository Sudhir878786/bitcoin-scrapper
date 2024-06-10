from django.db import models
import uuid

class Job(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Task(models.Model):
    job = models.ForeignKey(Job, related_name='tasks', on_delete=models.CASCADE)
    coin = models.CharField(max_length=10)
    output = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
