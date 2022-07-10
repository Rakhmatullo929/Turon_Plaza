from django.shortcuts import render
from plaza.models import Slide


# Create your views here.


def home_plaza(request):
    slides = Slide.objects.all()
    return render(request, 'home_plaza.html', {'slides': slides})


def room_plaza(request):
    return render(request, 'rooms_plaza.html')