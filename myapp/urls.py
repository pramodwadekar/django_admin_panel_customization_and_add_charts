from django.urls import path, include
from .import views

urlpatterns = [
    path("",views.index, name = 'index'),
    path("chart/", views.pie_chart, name = 'chart')
    
]