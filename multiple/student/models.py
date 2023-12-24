from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField("student name",max_length=50)
    division = models.CharField("student class",max_length=50)

def __str__(self):
    return self.Student
