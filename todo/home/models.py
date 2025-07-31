from django.db import models

# Create your models here.
class Task(models.Model):
    
    name = models.TextField(max_length=100)
    complete = models.BooleanField(default=False)
    important = models.BooleanField(default = False)

    def __str__(self):
        return self.name

   


