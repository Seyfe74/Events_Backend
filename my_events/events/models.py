from django.db import models
from django.contrib.auth.models import User

class EventCategory(models.Model):
    event_category = models.CharField(max_length=50) 

class Event(models.Model):
    event = models.CharField(max_length=50)
    event_timeInPT = models.DateTimeField()
    event_timestamp = models.CharField(max_length=50)
    event_videoId = models.CharField(max_length=50)
    event_category = models.ForeignKey(EventCategory, on_delete=models.CASCADE)

class TeamOrAthlet(models.Model):
    teamOrAthlet =models.CharField(max_length=50) 
    event_category = models.ForeignKey(EventCategory, on_delete=models.CASCADE)

class Customer (models.Model): 
    timezone =models.CharField(max_length=50) 
    location_state = models.CharField(max_length=50)
    template_id = models.CharField(max_length=50, default ='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event_category = models.ForeignKey(EventCategory,  on_delete=models.CASCADE)
    teamOrAthlet = models.ForeignKey(TeamOrAthlet,  on_delete=models.CASCADE) 
    
class ChoosenEvent(models.Model): 
    reminder_note = models.CharField(max_length=50)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

class Comment(models.Model):
    content = models.CharField(max_length=50)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

class Reply(models.Model):
    content = models.CharField(max_length=50)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    


    





    




