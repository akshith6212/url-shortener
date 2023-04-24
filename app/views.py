from django.http.response import HttpResponse
from django.shortcuts import render,redirect
import string,random,requests

from .models import Short
from django.contrib import messages

# Create your views here.
def index(request):
  if request.method == "POST":
    linkg = request.POST['urllink']
    if request.user.is_authenticated:
      try:
        response = requests.get(linkg)
        print(response)
        if len(Short.objects.filter(initurl=linkg)) != 0:
          link = Short.objects.filter(initurl=linkg)[0].shortenurl
        else:
          link = ''.join(random.choices(string.ascii_uppercase  + string.ascii_lowercase + string.digits, k = 6))
          while(len(Short.objects.filter(shortenurl = link)) != 0):
            link = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k = 6))
          author = request.user.username
          short = Short(initurl=linkg, shortenurl=link, author=author)
          short.save()
      except:
        messages.info(request,'Invalid Link')
        link = "home"
        print("in except statement")
        return redirect('/')
      return render(request, 'app/index.html',{'link':'http://localhost:8000/'+link})
    else:
      messages.info(request,'Please login/register')
      link = "home"
      print("in un authenticated else statement")
      return redirect('/')
  else:
    link = "http://localhost:8000/home/"
    return render(request, 'app/index.html',{'link':link})


def shortenurl(request,id):
  if len(Short.objects.filter(shortenurl=id)) != 0:
    print("here in if" + id)
    link = Short.objects.filter(shortenurl=id)[0].initurl
    return redirect(link)
  else:
    print("here in else" + id)
    return render(request, 'app/404.html')
