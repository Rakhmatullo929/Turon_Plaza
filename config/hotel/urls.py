from django.urls import path
from . import views

urlpatterns = [
    path('home_hotel/', views.home_hotel, name='home_hotel'),
    path('about_hotel/', views.about_hotel, name='about_hotel'),
    path('contact_us_hotel/', views.contact_us_hotel, name='contact_us_hotel'),
    path('rooms_hotel_hotel/', views.rooms_hotel, name='rooms_hotel'),
]
