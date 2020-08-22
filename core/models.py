from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=256,unique=True)

    def __str__(self):
        return self.title

# Create your models here.
