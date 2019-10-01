from django.db import models

gender_choice=(
    ('M','MALE'),
    ('F','FEMALE'),
    ('O','OTHERS')
)
# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=30)
    rollno=models.CharField(max_length=10)
    address=models.TextField()
    course=models.CharField(max_length=50)
    gender=models.CharField(max_length=1,choices=gender_choice,default='M')

class Teacher(models.Model):
    tname=models.CharField(max_length=30)
    code=models.CharField(max_length=10)
    salary=models.CharField(max_length=30)
    dept=models.CharField(max_length=10)
