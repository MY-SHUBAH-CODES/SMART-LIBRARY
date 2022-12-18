from django.urls import path
from app1 import views
urlpatterns = [
    path('',views.home,name='home'),
    path('todayspecial/',views.todayspecial,name='todayspecial'),
    path('davailable/',views.davailable,name='davailable'),
    path('booked/',views.booked,name='booked'),
    path('premium/',views.premium,name='premium'),
    path('about/',views.about,name='about'),







]