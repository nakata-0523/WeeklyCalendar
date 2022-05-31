from django.contrib import admin
from django.urls import path, include
from .views import WeekCalendar

urlpatterns = [
    path('week/', WeekCalendar.as_view(), name='week'),
    path('week/<int:year>/<int:month>/<int:day>/', WeekCalendar.as_view(), name='week'),
]
