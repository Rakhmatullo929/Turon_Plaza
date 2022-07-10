from django.shortcuts import render
from hotel.models import *
from . import forms


# Create your views here.


def home_hotel(request):
    return render(request, 'home_hotel.html')


def rooms_hotel(request):
    room = Room.objects.all()
    types = Type.objects.all()
    return render(request, 'rooms_hotel.html',
                  {'types': types, 'room': room})


def about_hotel(request):
    return render(request, 'about_hotel.html')


def contact_us_hotel(request):
    form = forms.FeedbackForms(request.POST or None)
    is_success = False
    if request.method == 'POST' and form.is_valid():
        is_success = True
        form.save()
        form = forms.FeedbackForms()
    return render(request, 'contact_us_hotel.html', {'form': form, 'is_success': is_success})
