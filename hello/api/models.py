from django.db import models

class Student(models.Model):
    name=models.TextField(max_length=200)
    roll_no=models.IntegerField()
    city=models.TextField()

# Create your models here.
