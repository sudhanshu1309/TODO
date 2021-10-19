from django.db import models

class Todo(models.Model):
    title = models.TextField(max_length=256)
    # description = models.TextField(max_length=256)
    timestamp = models.DateTimeField(auto_now_add=True)
    isDone = models.BooleanField(default=False)
