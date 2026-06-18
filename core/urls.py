from django.contrib import admin
from django.urls import path

from . import views
urlpatterns = [
   
    path('', views.home , name='home'),
    path('map/', views.map, name='map'),
    path('hki/', views.hki, name='hki'),
    path('certification/', views.certification, name='certification'),
    path('journal/', views.journal, name='journal'),
    path('conference/', views.conference, name='conference'),
]