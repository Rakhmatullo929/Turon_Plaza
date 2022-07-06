from django.shortcuts import render


# Create your views here.


def home_hotel(request):
    return render(request, 'home_hotel.html')


def about_hotel(request):
    return render(request, 'about_hotel.html')


def contact_us_hotel(request):
    return render(request, 'contact_us_hotel.html')