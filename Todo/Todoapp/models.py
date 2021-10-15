from django.db import models
from datetime import datetime

# Create your models here.


class Todo(models.Model):
    task = models.CharField(max_length=200)
    Create_at = models.DateTimeField(default=datetime.now,blank=True)

    def __str__(self):
        return self.task