from rest_framework import serializers
from .models import Sensor, Measurement


class MeasurementSerializer(serializers.ModelSerializer):
    sensor_id = serializers.PrimaryKeyRelatedField(queryset=Sensor.objects.all(), source='sensor', write_only=True)

    class Meta:
        model = Measurement
        fields = ['temperature', 'created_at', 'sensor_id']


class SensorSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']
