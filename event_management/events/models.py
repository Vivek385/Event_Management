# events/models.py
from django.db import models

class Venue(models.Model):
    Capacity = models.PositiveIntegerField()
    Venue_name = models.CharField(max_length=255)
    Location = models.CharField(max_length=255)

class Event(models.Model):
    Event_Name = models.CharField(max_length=255)
    Event_Duration = models.DurationField()
    Event_Date = models.DateField()
    Description = models.TextField()
    Venue_ID = models.ForeignKey(Venue, on_delete=models.CASCADE)

class Organiser(models.Model):
    UserName = models.CharField(max_length=255)
    Email = models.EmailField()
    Phone = models.CharField(max_length=15)

class Committee(models.Model):
    Event_ID = models.ForeignKey(Event, on_delete=models.CASCADE)
    Org_ID = models.ForeignKey(Organiser, on_delete=models.CASCADE)

class Attendee(models.Model):
    Attendee_Name = models.CharField(max_length=255)
    AttendeeEmail = models.EmailField()
    AttendeePhone = models.CharField(max_length=15)
    
class Registration(models.Model):
    Tickettype = models.CharField(max_length=255)
    RegistrationDate = models.DateTimeField(auto_now_add=True)
    Event_ID = models.ForeignKey(Event, on_delete=models.CASCADE)
    Attendee_ID = models.ForeignKey(Attendee, on_delete=models.CASCADE)


