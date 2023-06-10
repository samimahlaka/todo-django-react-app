from django.db import models
class Todo (models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField()
    completed = models.BooleanField(default='false')

    def __str__(self):
        return self.title






# Create your models here.
