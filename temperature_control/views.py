from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Temp_control_screen(request):
    return render(request, 'main_screen.html')

def set_PID_HAT(request):
    return render(request, 'HAT_control.html')

def set_PID_STANFORD(request):
    return render(request, 'STANFORD_control.html')