from django.contrib import admin
from.models import *



class SeatAdmin(admin.ModelAdmin):
    list_display = ('seat_number', 'creted_date', 'seat_discription')
admin.site.register(Seat,SeatAdmin)




