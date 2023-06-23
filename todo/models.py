from django.db import models
from django.contrib.auth.models import User
class Todo (models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField()
    completed = models.BooleanField(default='false')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title






# Create your models here.
