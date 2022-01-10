from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def fnindex(request):
    return HttpResponse("Hello this is my app")
