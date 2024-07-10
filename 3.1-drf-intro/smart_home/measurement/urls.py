from django.urls import path
from .views import SensorsView, SensorView, CreateSensor, UpdateSensor, AddMeasurement

urlpatterns = [
    path('sensors/', SensorsView.as_view()),
    path('sensor/<pk>/', SensorView.as_view()),
    path('cr/', CreateSensor.as_view()),
    path('up/<pk>/', UpdateSensor.as_view()),
    path('add/<pk>/', AddMeasurement.as_view()),
]
