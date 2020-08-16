from django.contrib import admin
from django.urls import path
from .views import test_view

urlpatterns = [
    path('', test_view),
    path('pie-chart/', user_views.pie_chart, name='pie-chart'),

]
