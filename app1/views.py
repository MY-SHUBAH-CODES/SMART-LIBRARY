from django.shortcuts import render,redirect
from django.http.response import HttpResponse
import datetime
import time
from app1.models import *
# Create your views here.
def home(request):
    return render(request,"index.html")


        

            
    # return render(request,'index.html',{'date':date})




def davailable(request,):
    list1=[]
    allobj=Seat.objects.all()
    for i in allobj:
        for j in range(3):
            if j==0:
                dic={"seat_number":str(i.seat_number),"slot":str(i.slot1)}

            elif j==1:
                dic={"seat_number":str(i.seat_number),"slot":str(i.slot2)}
            elif j==2:
                dic={"seat_number":str(i.seat_number),"slot":str(i.slot3)}

            list1.append(dic)
    list2=[]
    mydate=datetime.datetime.today().strftime('%Y-%m-%d')
    allobj1=AllBooking.objects.filter(check_in_date=mydate)
    for k in allobj1:
        dic1={"seat_number":str(k.Seat_number),"slot":str(k.Slot)}
        list2.append(dic1)

    return render(
    request,
    'availableseat.html',
    context={
    'obj':list1,        
    'obj1':list2, 
            }
       )
    




def davailable2(request):
    if request.method=='POST':
        list1=[]
        allobj=Seat.objects.all()
        for i in allobj:
            for j in range(3):
                if j==0:
                    dic={"seat_number":str(i.seat_number),"slot":str(i.slot1)}

                elif j==1:
                    dic={"seat_number":str(i.seat_number),"slot":str(i.slot2)}
                elif j==2:
                    dic={"seat_number":str(i.seat_number),"slot":str(i.slot3)}

                list1.append(dic)
        dt=request.POST['dt']
        list2=[]
        allobj1=AllBooking.objects.filter(check_in_date=dt)
        for k in allobj1:
            dic1={"seat_number":str(k.Seat_number),"slot":str(k.Slot)}
            list2.append(dic1)
        
    return render(
    request,
    'availableseat2.html',
    context={
    'obj':list1,        
    'obj1':list2, 
            }
       )


def todayspecial (request):
    return render(request,'todayspecial.html')

def Booking(request):
    return HttpResponse("uguyg")

def booked (request):
    return render(request,'bookedseat.html')

def premium (request):
    return render(request,'premiumseat.html')

def about (request):
    return render(request,'about.html')

