from django.db import models
from django.contrib.auth.models import User
# from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class Station(models.Model):
    code = models.CharField(max_length=124) # stasjonens navn
    city = models.CharField(max_length=124) # by

    def __str__(self):
        return  f"{self.code}"

# Togturer/ruter
class Ride(models.Model):
    origin = models.ForeignKey(Station, on_delete=models.CASCADE, related_name="dapartures", max_length=124)
    destination = models.ForeignKey(Station, on_delete=models.CASCADE, related_name="arrivals", max_length=124)
    date = models.DateField(blank=True, null=True) # dato for reisee
    time_start = models.TimeField(blank=True, null=True) # reise start
    time_end = models.TimeField(blank=True, null=True) # reise slutt
    # duration_h = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(24)])
    # duration_m = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(59)])
    price = models.FloatField(blank=True, null=True)


    def __str__(self):
        return f"{self.id} {self.origin} to {self.destination}. Date: {self.date}. Depart {self.time_start}"

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=124, null=True)
    email = models.CharField(max_length=124, null=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=124, null=True)

    def __str__(self):
        return str(self.id)


class OrderTicket(models.Model):
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
    date_added = models.DateTimeField(auto_now=True)
