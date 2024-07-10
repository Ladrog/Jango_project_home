from django.utils import timezone
from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Measurement(models.Model):
    sensor = models.ForeignKey('Sensor', related_name='measurements', on_delete=models.CASCADE)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        self.created_at = timezone.now()
        super(Measurement, self).save(*args, **kwargs)
