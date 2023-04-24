from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

import uuid

from .views import data, index, user


app_name = 'RobotMonitor'
urlpatterns = [
    path('refresh_token', TokenRefreshView.as_view()),
    path('get_public_key', user.GetPublicKey.as_view()),

    path('user/user_login', user.UserLogin.as_view()),
    path('user/user_logout', user.UserLogout.as_view()),

    path('user/create', user.CreateUser.as_view()),
    path('user/get', user.GetUserData.as_view()),
    path('user/change_password', user.ChangePassword.as_view()),

    path('data/get_robots', data.GetRobots.as_view()),
    path('data/get_available_data_time_ranges',
         data.GetAvailableTimeRanges.as_view()),
    path('data/get_data',
         data.GetData.as_view()),
    
    path('', index.index, name="index"),
    path('index', index.index, name="index"),
    path('login', index.login, name="login"),
    path('documentation', index.documentation, name="documentation"),
    path('api', index.api, name="api"),
    path('spot', index.spot, name="spot"),
    path('diagraph', index.diagraph, name="diagraph"),
    path('map', index.map, name="map"),
    
]
