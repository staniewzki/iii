from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class AppUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)

class Offer(models.Model):
    owner = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)

class Booking(models.Model):
    owner = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    begin = models.DateField()
    end = models.DateField()

class Availability(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    begin = models.DateField()
    end = models.DateField()
