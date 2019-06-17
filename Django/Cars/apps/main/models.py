from django.db import models

# Create your models here.
class Driver(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)

    # owned_cars => [Car, Car, Car]

    # def __str__(self):
    #     return f"{self.first_name} {self.last_name}"

class Car(models.Model):
    make = models.CharField(max_length=45)
    model = models.CharField(max_length=45)
    top_speed = models.FloatField() # 120.8

    owner = models.ForeignKey(Driver, related_name="owned_cars")
    # owner_id
