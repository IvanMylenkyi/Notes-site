from django.db import models
from django.urls import reverse

# Create your models here.

# Create a task model
class Task(models.Model):
    title = models.CharField('Name', max_length=40)
    task =  models.TextField('Description')

  
    def __str__(self):


        return self.title
    class Meta:
        verbose_name='Task'
        verbose_name_plural='Tasks'

    def get_absolute_url(self):
        return f'/task/{self.id}'
