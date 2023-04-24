from django.http import HttpResponse, JsonResponse, FileResponse
import json
from django.db.utils import IntegrityError
from datetime import datetime, date, timedelta

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


# class GetAvailableTimeRanges(APIView):
#     permission_classes = (IsAuthenticated,)
#
#     def get(self, request):
#         return HttpResponse("ANYTHING GOES")
#
#
# class GetData(APIView):
#     permission_classes = (IsAuthenticated,)
#
#     def get(self, request):
#         return HttpResponse()

def getTimeRanges(request):

    with open("static/times.json") as j:
        data = json.load(j)

    return JsonResponse(data, safe=False)

def getData(request):

    with open("static/sample.json") as j:
        data = json.load(j)

    return JsonResponse(data, safe=False)
