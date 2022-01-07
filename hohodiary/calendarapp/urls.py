from django.urls import path
from calendarapp.views import calendar
app_name = 'calendarapp'

urlpatterns = [
    path('calendar/', calendar, name='calendar'),
    
]