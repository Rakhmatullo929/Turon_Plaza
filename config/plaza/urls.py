from django.urls import path
from . import views

urlpatterns = [
    path('home_plaza/', views.home_plaza, name='home_plaza'),
    path('room_plaza/', views.room_plaza, name='room_plaza'),
    path('facilities_plaza/', views.facilities_plaza, name='facilities_plaza'),
    path('contact_us_plaza/', views.contact_us_plaza, name='contact_us_plaza'),
]
