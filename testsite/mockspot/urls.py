from django.urls import path
from . import views

app_name = 'mockspot'
urlpatterns = [

    path('', views.index, name="index"),
    path('index', views.index, name="index"),
    path('getCSV', views.getCSV, name="getCSV"),
    path('getImages', views.getImages, name="getImages"),
]
