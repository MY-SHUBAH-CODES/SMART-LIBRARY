from django.contrib import admin
from.models import *



class SeatAdmin(admin.ModelAdmin):
    list_display = ('seat_number', 'creted_date', 'seat_discription',"slot1","slot2","slot3")
admin.site.register(Seat,SeatAdmin)

class AllBookingAdmin(admin.ModelAdmin):
    list_display = ('check_in_date', 'Seat_number', 'Slot','userID','bookingid','booking_date')
admin.site.register(AllBooking,AllBookingAdmin)






