from django.urls import path
from . import views

urlpatterns = [
    path('home_plaza/', views.home_plaza, name='home_plaza'),
    path('room_plaza/', views.room_plaza, name='room_plaza')
]
