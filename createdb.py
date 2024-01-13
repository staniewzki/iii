from django.contrib.auth.models import User
from offers.models import *
import datetime

def create_user(username, password, name, email, phone_number):
    user = User.objects.create_user(username=username, password=password, first_name=name, email=email)
    user.save()
    return AppUser(user=user, phone_number=phone_number)

renter = create_user('koparkopol', 'lubie_koparki', 'Koparkopol', 'kontakt@koparkopol.pl', '+48123456789')
rentee = create_user('jan', '123456', 'Jan', 'jk123456@students.mimuw.edu.pl', '+48987654321')
renter.save(), rentee.save()

offer = Offer(owner=renter, name='Wielka kopara', kind='Excavator', description='To jest wielka kopara.')
offer.save()

Availability(offer=offer, begin=datetime.date(2024, 1, 20), end=datetime.date(2024, 2, 20)).save()
Availability(offer=offer, begin=datetime.date(2024, 2, 25), end=datetime.date(2024, 3, 25)).save()