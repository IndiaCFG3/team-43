from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from .models import *
# Create your views here.
@login_required
def dashboard(request):
    # if request.user.Profile.usertype == 'admin':
    #     # do database operations and create context
    #     return render(request,"users/dashboard.html", {message:"You're admin"})
    if request.user.Profile.usertype == 'audit':
        output = Student_Display()
        # do database operations and create context
        return render(request,"users/dashboard.html", {'output':output})
    if request.user.Profile.usertype == 'HR':
        output = Employee_Display()
        # do database operations and create context
        return render(request,"users/dashboard.html", {'output':output})
    
