from django.shortcuts import render
from plaza.models import Slide


# Create your views here.


def home_plaza(request):
    slides = Slide.objects.all()
    return render(request, 'home_plaza.html', {'slides': slides})


def room_plaza(request):
    return render(request, 'rooms_plaza.html')


def facilities_plaza(request):
    return render(request, 'facilities_plaza.html')


def contact_us_plaza(request):
    return render(request, 'contact_us_plaza.html')
