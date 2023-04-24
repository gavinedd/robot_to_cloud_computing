from rest_framework.test import APIRequestFactory

from random import randint, choice
from uuid import uuid4
from datetime import datetime, date

from ..models import FrontendUser
from ..views import user as user_views


def generate_random_email():
    return str(uuid4()) + 've{ry."(),:;<>[]".VER}Y."ver\\\\\\ y@\\"very".unusual@strange.example.com'

def generate_random_name():
    return 'Name-' + str(uuid4())[:33] + "'d"

def generate_random_date():
    year = randint(1920, 2021)
    month = randint(1, 12)
    day = randint(1, 28)
    return datetime.strptime(f'{year}-{month}-{day}', '%Y-%m-%d').date()

def generate_random_password():
    special_chars = ['~', '`', '!', '@', '#', '$', '%', '^', '&', '*',
                     '(', ')', '_', '-', '=', '+', '{', '}', '|', '[', ']', ';', '\'', ':',
                     '"', '<', '>', '?', ',', '.', '/']

    return 'UPPERlower' + choice(special_chars) + str(randint(0, 99)) + str(uuid4())

def generate_random_user(**kwargs):
    user_id = uuid4()

    user_data = {'id': user_id, 'is_active': True, 'email': generate_random_email(), 'first_name':
                 generate_random_name(), 'last_name': generate_random_name(), 'date_of_birth':
                 generate_random_date(), 'password': generate_random_password()}

    for key, value in kwargs.items():
        user_data[key] = value

    return user_data

def create_user(**kwargs):
    factory = APIRequestFactory()

    user = generate_random_user(**kwargs)

    request = factory.post('/RobotMonitor/user/create', user)
    user_views.CreateUser.as_view()(request)

    return FrontendUser.objects.get(pk=user['id'])
