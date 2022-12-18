from django.shortcuts import render
from django.http.response import HttpResponse
import datetime
from app1.models import *

# Create your views here.
def home(request):
    date=datetime.date
    return render(request,'index.html',{'date':date})


def todayspecial (request):
    return render(request,'todayspecial.html')

def davailable (request,):
    objseat=Seat.objects.all()
    return render(request,'availableseat.html',{'obj':objseat})

def booked (request):
    return render(request,'bookedseat.html')

def premium (request):
    return render(request,'premiumseat.html')

def about (request):
    return render(request,'about.html')

