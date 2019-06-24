from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def myView2(request):
    return render(request,'display.html')