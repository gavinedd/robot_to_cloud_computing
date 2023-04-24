from django.urls import path
from .views import data, index

app_name = 'RobotMonitor'
urlpatterns = [
    # path('data/get_available_data_time_ranges/<uuid:robot_id>',
    #      data.GetAvailableTimeRanges.as_view()),
    # path('data/get_data/<uuid:robot_id>&start=<str:start_time>&end=<str:end_time>',
    #      data.GetData.as_view()),

    path('data/get_available_data_time_ranges', data.getTimeRanges, name="gettimeranges"),
    path('data/get_data', data.getData, name="getdata"),

    path('data/get_available_data_time_ranges/<uuid:robot_id>', data.getTimeRanges, name="gettimeranges"),
    path('data/get_data/<uuid:robot_id>&start=<str:start_time>&end=<str:end_time>', data.getData, name="getdata"),


    path('', index.index, name="index"),
    path('index', index.index, name="index"),
]
