from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def linkedinfn(request):
   # return HttpResponse("Hello welcome to Linkedin user Login page")
   return render(request,'login.html')

def loginfn(request):
    return render(request,'login.html')


