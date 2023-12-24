from django.db import models

# Create your models here.

class Teacher(models.Model):
    name = models.CharField("student name",max_length=50)
    rank = models.CharField("student class",max_length=50)

def __str__(self):
    return self.Teacher
