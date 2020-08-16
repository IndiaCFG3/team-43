from django.shortcuts import render
from .csv_to_db import db_save
from django.http import HttpResponse
from .models import Student,Employee,BatchStudent

# Create your views here.
def test_view(request):
    flag = db_save()
    students = Student.objects.all()
    emp = Employee.objects.all()
    b_s = BatchStudent.objects.all()
    html = str.format("<html><body>Saved {} {} {}</body></html>" , students,emp, flag)
    return HttpResponse(html)