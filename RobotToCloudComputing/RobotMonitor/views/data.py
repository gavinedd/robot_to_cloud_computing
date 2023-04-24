from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseNotFound, HttpResponse
from django.db.utils import IntegrityError
from datetime import datetime, date, timedelta, timezone
from django.conf import settings

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from ..csv import csvtojson

from ..models import CsvFile, RobotImageFile, Robot

import json
import os


class GetRobots(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):

        robots = Robot.objects.all()

        robot_data = list()
        for robot in robots:
            robot_data.append(
                dict(
                    name=robot.name,
                    id=str(robot.id),
                ))

        robot_data_as_json = json.dumps(robot_data)

        return HttpResponse(robot_data_as_json)


class GetAvailableTimeRanges(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):

        robot_id = request.GET['robot_id']

        robot_data = list()

        csv_files = CsvFile.objects.filter(robot_id=robot_id)

        for file in csv_files:
            robot_data.append(
                dict(
                    start_time = str(file.start_timestamp.timestamp()),
                    end_time = str(file.end_timestamp.timestamp())
                )
            )

        robot_data_as_json = json.dumps(robot_data)

        return HttpResponse(robot_data_as_json)
        

class GetData(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):

        # Obtain necessary information from the request
        robot_id = request.GET['robot_id']
        start_time = float(request.GET['start_time'])
        end_time = float(request.GET['end_time'])
        
        data = []
        csv_files = CsvFile.objects.filter(robot_id=robot_id, start_timestamp__gte=datetime.fromtimestamp(start_time, tz=timezone.utc), end_timestamp__lte=datetime.fromtimestamp(end_time, tz=timezone.utc))
               
        # Obtain the csv files and images requested
        for csv_object in csv_files:
            files = {'csv': {
                'start_time': str(csv_object.start_timestamp.timestamp()),
                'end_time': str(csv_object.end_timestamp.timestamp()),
                'file': csv_object.file_path
            }}

            images_files = RobotImageFile.objects.filter(csv_file=csv_object.id)
            images = []
            
            for image in images_files:
                images.append({
                    'timestamp' : str(image.image_timestamp.timestamp()),
                    'file' : image.file_path,
                    'image_type' : image.image_type
                })
                
            files['images'] = images

            csv_file_path = str(settings.BASE_DIR).replace('\\', '/') + csv_object.file_path
            
            with open(csv_file_path, 'rb') as csvfile:
                files['data'] = json.loads(csvtojson.csv_to_json(csvfile.read(), as_str=True))

            data.append(files)
            
        return HttpResponse(json.dumps(data))
