from django.contrib import admin
from.models import *



class SeatAdmin(admin.ModelAdmin):
    list_display = ('seat_number', 'creted_date', 'seat_discription')
admin.site.register(Seat,SeatAdmin)

class AllBookingAdmin(admin.ModelAdmin):
    list_display = ('check_in_date', 'Seat_number', 'Slot')
admin.site.register(AllBooking,AllBookingAdmin)






