from django.db import models

# Create your models here.


class Note(models.Model):
    text = models.CharField(max_length=50, verbose_name="Enter your note here")
    time_of_posting = models.DateTimeField()
