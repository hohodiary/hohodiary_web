from django.shortcuts import render

# Create your views here.
def calendar(request):
    return render(request, 'calendarapp/calendar.html')
