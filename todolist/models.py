from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    is_finished = models.BooleanField(default=False)
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()