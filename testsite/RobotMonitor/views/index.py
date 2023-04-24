from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("I am a test server API for RobotMonitor, and robot communication testing")

# Create your views here.
