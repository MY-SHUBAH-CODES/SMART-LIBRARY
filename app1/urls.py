from django.urls import path
from app1 import views
urlpatterns = [
    path('',views.home,name='home'),
    path('todayspecial/',views.todayspecial,name='todayspecial'),
    path('davailable/',views.davailable,name='davailable'),
    path('davailable2/',views.davailable2,name='davailable2'),
    path('booking/',views.Booking,name='Booking'),


    path('booked/',views.booked,name='booked'),
    path('premium/',views.premium,name='premium'),
    path('about/',views.about,name='about'),







]