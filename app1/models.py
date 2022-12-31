from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Seat(models.Model):
    seat_number=models.IntegerField(primary_key=True,auto_created=True)
    creted_date=models.DateTimeField(auto_created=True)
    seat_discription=models.CharField(max_length=1000)
    slot1=models.IntegerField()
    slot2=models.IntegerField()
    slot3=models.IntegerField()
    def seatnum(self):
        return self.seat_number
    
class AllBooking(models.Model):
    bookingid=models.AutoField(primary_key=True)
    userID = models.CharField(max_length=50,default='NA')
    check_in_date=models.DateField()
    Seat_number=models.IntegerField()
    Slot=models.IntegerField()
    booking_date=models.CharField(max_length=50,default="NA")
    
    

    
    