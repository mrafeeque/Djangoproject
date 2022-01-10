from django.shortcuts import render

# Create your views here.

def signupfn(request):
    return render(request,'signup.html')