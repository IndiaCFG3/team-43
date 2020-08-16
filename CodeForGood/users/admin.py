from django.contrib import admin

# Register your models here.
from .models import Profile,Student,Employee,BatchStudent


admin.site.register(Profile)
admin.site.register(Student)
admin.site.register(Employee)
admin.site.register(BatchStudent)
