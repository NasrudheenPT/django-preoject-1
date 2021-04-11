from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=30,verbose_name="student name")
    age=models.IntegerField(default=0,verbose_name="Age")
    email=models.EmailField(max_length=50)

class img(models.Model):
    image = models.FileField(upload_to='user',max_length=300)
    Student = models.ForeignKey(Student,on_delete=models.CASCADE)