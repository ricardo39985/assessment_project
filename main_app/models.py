from django.db import models

# Create your models here.
class List(models.Model):
    description = models.TextField(max_length=200)

    def __str__(self):
        return f"{self.description}"

