from django.db import models

class Kettle(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=80)
    sensor_id = models.CharField(max_length=80)
    heater = models.CharField(max_length=10)
    automatic = models.CharField(max_length=255)
    agitator = models.CharField(max_length=10)
    target_temp = models.IntegerField()
    height = models.IntegerField()
    diameter = models.IntegerField()

    def __unicode__(self):
        return self.name

class
