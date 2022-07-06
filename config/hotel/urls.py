from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home_hotel, name='home_hotel'),
    path('about/', views.about_hotel, name='about_hotel'),
    path('contact_us/', views.contact_us_hotel, name='contact_us_hotel')
]
