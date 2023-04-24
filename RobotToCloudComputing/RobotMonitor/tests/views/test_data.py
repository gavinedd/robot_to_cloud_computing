from urllib import request
from uuid import uuid4
from datetime import date, timedelta, timezone, datetime
from json import loads, JSONDecodeError
from pytz import UTC
from django.conf import settings

import json

from django.test import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate
from django.utils.timezone import now, datetime
from .. import test_utils
from ...models import CsvFile, RobotImageFile, Robot, FrontendUser
from ...views import user as user_views
from ...views import data as data_views
from rest_framework_simplejwt.views import TokenRefreshView
from ...csv import csvtojson

class TestDataViews(TestCase):
    def test_get_available_time_range(self):
        factory = APIRequestFactory()

        user = test_utils.generate_random_user()
        test_utils.create_user(**user)


        for robot in Robot.objects.all():
            robot_id = str(robot.id)

            # test = "bf3b4862-d905-4f57-b9ae-2297685d2b8c"

            request = factory.get("/RobotMonitor/data/get_available_data_time_ranges?robot_id=" + robot_id, format='json')
            force_authenticate(request, user=FrontendUser.objects.get(pk=user['id']))
            response = data_views.GetAvailableTimeRanges.as_view()(request)

            self.assertEqual(response.status_code, 200)

            decoded_response = response.content.decode('UTF-8')

            data = json.loads(decoded_response)

            csvs = CsvFile.objects.get(robot_id=robot_id)

            self.assertEqual(data[0]['start_time'], str(csvs.start_timestamp.timestamp()))
            self.assertEqual(data[0]['end_time'], str(csvs.end_timestamp.timestamp()))

            
    def test_get_data_between_time_ranges(self):
        factory = APIRequestFactory()

        user = test_utils.generate_random_user()
        test_utils.create_user(**user)
        
        robot_id = 'bf3b4862-d905-4f57-b9ae-2297685d2b8c'
        start_time = 1644100124.938643
        end_time = 1644100139.8638778
        
        csv_files = CsvFile.objects.filter(robot_id=robot_id, start_timestamp__gte=datetime.fromtimestamp(
          start_time, tz=timezone.utc), end_timestamp__lte=datetime.fromtimestamp(end_time, tz=timezone.utc))

        request = factory.get(
          f"/RobotMonitor/data/get_data?robot_id={robot_id}&start_time={start_time}&end_time={end_time}", format='json')
        force_authenticate(request, user=FrontendUser.objects.get(pk=user['id']))
        
        response = data_views.GetData.as_view()(request)
        
        self.assertEqual(response.status_code, 200)

        decoded_response = response.content.decode('UTF-8')
        data = json.loads(decoded_response)
        for i in range(len(data)):
            self.assertGreaterEqual(float(data[i]['csv']['start_time']), csv_files[i].start_timestamp.timestamp())
            self.assertLessEqual(float(data[i]['csv']['end_time']), csv_files[i].end_timestamp.timestamp())
          
            images = RobotImageFile.objects.filter(csv_file=csv_files[i].id)
            for j in range(len(data[i]['images'])):
                self.assertEqual(float(data[i]['images'][j]['timestamp']), images[j].image_timestamp.timestamp())
                self.assertEqual(data[i]['images'][j]['image_type'], images[j].image_type)
              
            csv_file_path = str(settings.BASE_DIR).replace('\\', '/') + csv_files[i].file_path 
            
            with open(csv_file_path, 'rb') as csvfile:
                self.assertEqual(json.loads(csvtojson.csv_to_json(csvfile.read(), as_str=True)), data[i]['data'])

               
    def test_get_robots(self):
        """
        get_robots endpoint correctly returns a list of robot ids and names
        """
        factory = APIRequestFactory()

        user = test_utils.generate_random_user()

        create_user_request = factory.post('/RobotMonitor/user/create', user)
        create_user_response = user_views.CreateUser.as_view()(create_user_request)

        robots = Robot.objects.all()

        request = factory.get('/RobotMonitor/data/get_robots')
        force_authenticate(request, user=FrontendUser.objects.get(pk=user['id']))

        response = data_views.GetRobots.as_view()(request)

        self.assertEqual(response.status_code, 200)

        decoded_response = response.content.decode('UTF-8')
        robot_list = json.loads(decoded_response)

        for i in range(0, len(robot_list)):
          self.assertEqual(robot_list[i]['name'], robots[i].name)
          self.assertEqual(robot_list[i]['id'], str(robots[i].id))
          self.assertFalse(hasattr(robot_list[i], 'auth_string'))
