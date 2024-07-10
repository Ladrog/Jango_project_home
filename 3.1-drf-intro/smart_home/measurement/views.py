from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateAPIView, \
    CreateAPIView
from rest_framework.response import Response

from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer


class SensorsView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        sensors = response.data

        def exclude_measurements(sensor):
            sensor.pop('measurements', None)
            return sensor

        sensors_without_measurements = [exclude_measurements(sensor) for sensor in sensors]
        response.data = sensors_without_measurements

        return response


class SensorView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class CreateSensor(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class UpdateSensor(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class AddMeasurement(CreateAPIView):
    serializer_class = MeasurementSerializer

    def create(self, request, *args, **kwargs):
        sensor = self.get_object()
        data = request.data.copy()
        data['sensor_id'] = sensor.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_object(self):
        return Sensor.objects.get(pk=self.kwargs['pk'])
