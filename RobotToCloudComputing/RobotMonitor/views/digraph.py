import re
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'RobotMonitor/index.html')


def documentation(request):
    return render(request, 'RobotMonitor/documentation.html')


def login(request):
    return render(request, 'RobotMonitor/login.html')


def spot(request):
    return render(request, 'RobotMonitor/spot.html')


def diagraph(request):
    return render(request, 'RobotMonitor/diagraphTemplate.html')    

    
def map(request):
    return render(request, 'RobotMonitor/xyPlot.html')


def api(request):
    return JsonResponse


# Create your views here.
