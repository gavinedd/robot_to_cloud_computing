from django.shortcuts import render
from django.http import HttpResponse, FileResponse, JsonResponse


def index(request):
    return HttpResponse("This is Mockspot")


def getCSV(request):
    return FileResponse(open("static/csv/Grass_0.csv", 'rb'))


def getImages(request):
    return FileResponse(open('static/images.zip', 'rb'))
