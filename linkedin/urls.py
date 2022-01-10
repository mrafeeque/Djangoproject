from django.urls import path
from . import views

urlpatterns =[
    path('userlogin/',views.linkedinfn,name='userlogin'),
    path('loginpage/',views.loginfn,name='loginpage')
]
