from django.contrib import admin
from django.urls import path
from .views import test_view

urlpatterns = [
    path('', test_view),
    # path('score-chart/', views.score_chart, name='score-chart'),
]
