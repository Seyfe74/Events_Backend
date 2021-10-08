from django.db import models
from django.contrib.auth.models import User



class EventCategory(models.Model):
    event_categoryname = models.CharField(max_length=100)

class TimeZone(models.Model):
    timezone_name = models.CharField(max_length=100)

class Event(models.Model):
    event_category = models.ForeignKey(EventCategory, on_delete=models.CASCADE)
    time_zone = models.ForeignKey(TimeZone, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=100) 

class Location(models.Model):
    time_zone = models.ForeignKey(TimeZone, on_delete=models.CASCADE)
    state_name = models.CharField(max_length=50) 
    country_name = models.CharField(max_length=50)

class Customer (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time_zone = models.ForeignKey(TimeZone, on_delete=models.CASCADE)
    username = models.CharField(max_length=50) 
    email = models.CharField(max_length=50) 
    first_name = models.CharField(max_length=50) 
    last_name = models.CharField(max_length=50) 

class ChoosenEvent(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

class Comment(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    content = models.CharField(max_length=50)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

class Reply(models.Model):
    content = models.CharField(max_length=50)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)


    





    




