
from django.contrib import admin
from django.urls import path
from users import views as user_views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',user_views.register,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('profile/',user_views.profile,name='profile'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path('dashboard/',user_views.dashboard,name='dashboard'),
    path('test/',user_views.test_view,name='test'),
    path('studentList/',user_views.StudentListView.as_view(),name='student-list'),
    path('employeeList/',user_views.EmployeeListView.as_view(),name='employee-list'),



]
