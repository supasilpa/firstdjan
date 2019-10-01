from django.shortcuts import render
from django.http import HttpResponse
from .forms import Teacherform

# Create your views here.
def indexpage(request):
    return render(request,'index.html')
def contactpage(request):
    return render(request,'contact1.html')
def homepage(request):
    return render(request,'home.html')
def  teacherpage(request):
    form=Teacherform()
    return render(request,'teacher.html',{'form':form})