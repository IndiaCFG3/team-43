from django.db import models

class Employee(models.Model):
    employee_id = models.CharField(max_length=10, primary_key = True)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)

class Manager(models.Model):
    manager_id = models.CharField(max_length=10)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)


class HREmployees(models.Model):
    employee = models.OneToOneField(Employee)
    rating = models.IntegerField()
    manager = models.ForeignKey(Manager)
    leaves_taken = models.IntegerField()

class Course(models.Model):
    course_id = models.CharField(max_length = 10)
    name = models.TextField()

class HRStudents():
    course_id = models.ForeignKey(Course)
    batch_id = models.CharField(max_length = 10)
    no_of_students_joined = models.IntegerField()
    no_of_students_left = models.