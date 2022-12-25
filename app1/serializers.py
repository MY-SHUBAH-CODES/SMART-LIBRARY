from rest_framework import serializers
from app1.models import *
class SeattSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = ["seat_number","creted_date","seat_discription","slot1","slot2","slot3"]

class AllBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllBooking
        fields = ["check_in_date","Seat_number","Slot"]
        

