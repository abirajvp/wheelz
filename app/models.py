from django.db import models
from django.contrib.auth.models import User

class VehicleType(models.Model):
    name = models.CharField(max_length=100)

class Make(models.Model):
    name = models.CharField(max_length=100)

class Model(models.Model):
    name = models.CharField(max_length=100)

class Fuel(models.Model):
    name = models.CharField(max_length=100)

class Gearbox(models.Model):
    name = models.CharField(max_length=100)

class Car(models.Model):
    name = models.CharField(max_length=100)
    vehicle_id = models.CharField(max_length=32)
    used_car = models.BooleanField(default=False)
    new_car = models.BooleanField(default=False)
    automatic = models.BooleanField(default=False)
    manual = models.BooleanField(default=False)
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE, null=True, blank=True, default="No Information")
    make = models.ForeignKey(Make, on_delete=models.CASCADE, null=True, blank=True, default="No Information")
    model = models.ForeignKey(Model, on_delete=models.CASCADE, null=True, blank=True, default="No Information")
    price_amount = models.DecimalField(max_digits=16, decimal_places=2, null=True, blank=True)
    price_display = models.CharField(max_length=64, default="No Information")
    price_description = models.CharField(max_length=64, default="No Information")
    mileage = models.IntegerField()
    mileage_display = models.CharField(max_length=64, default="No Information")
    engine = models.CharField(max_length=32, default="No Information")
    power = models.CharField(max_length=64, default="No Information")
    fuel = models.ForeignKey(Fuel, on_delete=models.CASCADE, null=True, blank=True)
    gearbox = models.ForeignKey(Gearbox, on_delete=models.CASCADE, null=True, blank=True)
    doors = models.CharField(max_length=64, default="No Information")
    seats = models.CharField(max_length=64, default="No Information")
    color = models.CharField(max_length=64, default="No Information")
    registration_date = models.CharField(default="No Information")
    image = models.ImageField(upload_to='car_images/')
    image_src = models.TextField(null=True, blank=True)
    year = models.CharField(default="No Information")
    owner_name = models.CharField(max_length=128, default="No Information")
    owner_phone = models.CharField(max_length=32, default="No Information")
    owner_address = models.CharField(max_length=255, default="No Information")
    display_home = models.BooleanField(default=False)

class CarImage(models.Model):
    car = models.ForeignKey(Car, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='car_images/')
