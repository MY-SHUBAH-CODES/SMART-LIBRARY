from django.db import models

# Create your models here.

class Seat(models.Model):
    seat_number=models.IntegerField(primary_key=True,auto_created=True)
    creted_date=models.DateTimeField(auto_created=True)
    seat_discription=models.CharField(max_length=1000)
    slot1=models.BooleanField(default=True)
    slot2=models.BooleanField(default=True)
    slot3=models.BooleanField(default=True)
    def seatnum(self):
        return self.seat_number
    
    
    
    

    
    