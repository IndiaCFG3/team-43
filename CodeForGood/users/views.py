from django.shortcuts import render
from .csv_to_db import db_save
from django.http import HttpResponse
from .models import Student,Employee,BatchStudent
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from .models import *
from django.views.generic import ListView


# Create your views here.
def test_view(request):
    flag = db_save()
    students = Student.objects.all()
    emp = Employee.objects.all()
    b_s = BatchStudent.objects.all()
    html = str.format("<html><body>Saved {} {} {}</body></html>" , students,emp, flag)
    return HttpResponse(html)

# Create your views here.




@login_required
def dashboard(request):
    # if request.user.Profile.usertype == 'admin':
    #     # do database operations and create context
    #     return render(request,"users/dashboard.html", {message:"You're admin"})
    context={
        'students':Student.objects.all()
    }
    if request.user.profile.usertype == 'admin':
        output = Student_Display()
        # do database operations and create context
        return render(request,"users/dashboard.html", {'output':output})
    if request.user.profile.usertype == 'HR':
        output = Employee_Display()
        # do database operations and create context
        return render(request,"users/dashboard.html", {'output':output})
    
from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
	if request.method=='POST':
		form=UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username=form.cleaned_data.get('username')
			messages.success(request, f'Your account has been created! You are now able to login')
			return redirect('login')
	else:	
		form=UserRegisterForm()
	return render(request,'users/register.html',{'form':form})

@login_required
def profile(request):
	if request.method=='POST':
		u_form = UserUpdateForm(request.POST,request.FILES,instance=request.user)
		p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'Your account has been updated! You are now able to login')
			return redirect('profile')
	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)

	context={
		'u_form':u_form,
		'p_form':p_form
	}
	return render(request,'users/profile.html',context)    


class StudentListView(ListView):
    model=Student
    context_object_name='students'
    template_name='users/studentList.html'