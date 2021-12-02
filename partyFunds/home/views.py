from django.shortcuts import render
from .models import Employee

# Create your views here.

def index(request):
    data=Employee.objects.all()
    return render (request,'index.html',{'data':data})