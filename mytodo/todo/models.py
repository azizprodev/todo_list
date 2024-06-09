from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    completted = models.BooleanField(default=False)
    