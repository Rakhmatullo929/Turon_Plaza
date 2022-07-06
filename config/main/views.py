from django.shortcuts import render

# Create your views here.


def main_block(request):
    return render(request, 'main_block.html')
