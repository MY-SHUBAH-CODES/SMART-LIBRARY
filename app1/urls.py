from django.urls import path
from app1 import views
urlpatterns = [
    path('',views.home,name='home'),
    path('todayspecial/',views.todayspecial,name='todayspecial'),
    path('davailable/',views.davailable,name='davailable'),
    path('davailable2/',views.davailable2,name='davailable2'),
    path('booking/',views.booking,name='booking'),
    path('createbooking/',views.createbooking,name='createbooking'),
    path('mybooking/',views.mybooking,name='mybooking'),
    path('premium/',views.premium,name='premium'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('bookingnotallowed/',views.bookingnotallowed,name='bookingnotallowed'),
    path('logout/',views.logout,name='logout'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),

    






    







]