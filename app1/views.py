from django.shortcuts import render,redirect
from django.http.response import HttpResponse
import datetime
from app1.models import *
from django.contrib.auth import authenticate, login as li, logout as lo
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def home(request):
    return render(request,"home.html")


        

            
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
    'dt':mydate,
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
        if dt == "":
            return HttpResponse(" you are requesting for no date plese select a valid date!")
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
       'dt':dt ,  
             }
       )


def todayspecial (request):
    return render(request,'todayspecial.html')

def booking(request):
    if request.method=='POST':
        seat=request.POST['seat']
        slot=request.POST['slot']
        bdt=request.POST['bdate']
        stno=seat[5:]
        slotno=slot[5:]
    return render(request, 'booking.html',{'seat':stno,'slot':slotno,'bdt':bdt})

def createbooking(request):
    if request.method=='POST':
        list=[]
        flag=0
        date=request.POST['dt']
        seat=request.POST['seat']
        slot=request.POST['slot']
        mydate=datetime.datetime.today().strftime('%Y-%m-%d')

        allobj1=AllBooking.objects.filter(check_in_date=date)
        for k in allobj1:
            dic1={"seat_number":str(k.Seat_number),"slot":str(k.Slot)}
            list.append(dic1)
        list2=[{"seat_number":str(seat),"slot":str(slot)}]
        for i in list:
            if i in list2:
                flag+=1

        if request.user.is_authenticated and flag==0:
            obj=AllBooking(check_in_date=date,Seat_number=seat,Slot=slot,userID=request.user,booking_date=mydate)
            obj.save()
            return redirect('/mybooking/')
        elif request.user.is_authenticated==False:
            return redirect('/login/')
        elif flag!=0:
            return HttpResponse("this seat for the slot is  aleady booked")
        
def mybooking(request):
    if request.method=='GET':
        user=request.user
        mybooking=AllBooking.objects.filter(userID=user)
        
    return render(request,'mybooking.html',{'data':mybooking})

def premium (request):
    return render(request,'premiumseat.html')

def about (request):
    return render(request,'about.html')

def bookingnotallowed(request):
    return HttpResponse("this slot is already booked try to booked available slot")

def login(request):
    if request.method == 'POST':
        # Process the request if posted data are available
        username = request.POST['username']
        password = request.POST['password']
        # Check username and password combination if correct
        user = authenticate(username=username, password=password)
        if user is not None:
            # Save session as cookie to login the user
            li(request, user)
            # Success, now let's login the user.
            return render(request, 'index.html')
        else:
            # Incorrect credentials, let's throw an error to the screen.
            return render(request, 'login.html', {'error_message': 'Incorrect username and / or password.'})
    else:
        # No post data availabe, let's just show the page to the user.
        return render(request, 'login.html')

# ============================================================================


def logout(request):
    try:
        lo(request)
        response = {
            "status": "ok",
            "message": "user logged Out"
        }
    except:

        response = {
            "status": "error",
            "message": "kya kr rhe ho yaar!!"
        }
    return render(request,'index.html')

#======================================================================================


def signup(request):
    if request.method == "POST":
        if request.POST['password'] == request.POST['password_again']:
            try:
                User.objects.get(username=request.POST['username'])
                return render(request, 'signup.html', {'error_message': 'Username is already taken!'})
            except User.DoesNotExist:
                if len(request.POST['username']) < 5:
                    return render(request, 'signup.html', {'error_message': 'user name is too short'})

                if len(request.POST['password']) < 8:
                    return render(request, 'signup.html', {'error_message': 'password is too short'})

                else:
                    user = User.objects.create_user(request.POST['username'], request.POST['password'], request.POST['password_again'])
                # auth.login(request,user)
                    return render(request, 'login.html',{})
        else:
            return render(request, 'signup.html', {'error_message': 'Password does not match!'})
    else:
        return render(request, 'signup.html')



