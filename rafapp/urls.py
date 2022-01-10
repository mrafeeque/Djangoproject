
from django.urls import path
from . import views

urlpatterns=[
    path('home/',views.functionname,name='home')
] 