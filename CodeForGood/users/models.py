from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=10,default='First name')
    lastname=models.CharField(max_length=10,default='Last name')
    usertype=models.CharField(max_length=10,default='admin')
    phone_number=models.CharField(max_length=10,null=False, blank=False, unique=True)
    def __str__(self):
        return f'{self.user.username} Profile'

class Student(models.Model):
    student_id = models.CharField(max_length = 10)
    student_name = models.TextField()
    score = models.IntegerField()
    rating = models.IntegerField()
    performance = models.TextField()

class BatchStudent(models.Model):
    student_id = models.OneToOneField(Student,on_delete=models.CASCADE)
    batch_id =  models.CharField(max_length = 10)

class Employee(models.Model):
    employee_id = models.CharField(max_length = 10)
    employee_name = models.TextField()
    manager_name = models.TextField()
    leaves_taken = models.IntegerField()
    rating = models.IntegerField()

