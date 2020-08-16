from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    student_id = models.CharField(max_length = 10)
    first_name = models.CharField(max_length = 10)
    last_name = models.CharField(max_length = 10)
    email = models.CharField(max_length = 100, null = True)
    mobile_number = models.CharField(max_length = 10, null = True)
    

class Course(models.Model):
    course_id = models.CharField(max_length = 10)
    name = models.TextField()


class StudentCourse(models.Model):
    student_id = models.ForeignKey(Student)
    course_id = models.ForeignKey(Course)
    batch_id = models.CharField(max_length = 10)
    # for attendance we can include it here only ig
    attended = models.IntegerField()
    total_classes = models.IntegerField()

class Assessment(models.Model):
    student_course = models.ForeignKey(StudentCourse)
    name = models.CharField(max_length = 100)
    max_marks = models.DecimalField(max_digits=5, decimal_places=2)
    marks_obtained = models.DecimalField(max_digits=5, decimal_places=2)


