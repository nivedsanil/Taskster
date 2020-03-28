from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):

    username=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    date=models.DateTimeField(default=datetime.now, blank=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self): 
        return self.title
