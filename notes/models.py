from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Note(models.Model):

    username=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    date=models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self): 
        return self.title





