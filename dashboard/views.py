from django.shortcuts import render,redirect
from app.models import Short
from datetime import date

# Create your views here.
def index(request):
  months = ["Unknown",
          "January",
          "February",
          "March",
          "April",
          "May",
          "June",
          "July",
          "August",
          "September",
          "October",
          "November",
          "December"]

  if request.user.is_authenticated:
    name = request.user.username
    today = date.today()
    month = months[today.month]
    day = today.day
    links = Short.objects.filter(author=request.user.username)
    count = 0
    for link in links:
      count = count+1
    return render(request, 'dashboard/index.html', {'links':links,'count':count, 'month':month, 'day':day, 'name':name })
  else:
    return redirect(request,'/')