from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.utils.dateparse import parse_duration

def event_management(request):
    flag = 0
    if request.method == 'POST':
        form_identifier = request.POST.get('form_identifier')
        if ('form1' in request.POST) or (form_identifier == 'form1'):
            event_name = request.POST.get('event_name')
            event_duration = parse_duration(request.POST.get('event_duration'))
            event_date = request.POST.get('event_date')
            description = request.POST.get('description')
            organizer_name = request.POST.get('organizer_name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            capacity = int(request.POST.get('capacity'))
            venue_name = request.POST.get('venue_name')
            location = request.POST.get('location')
            print( event_name,'\n',event_duration ,'\n',event_date ,'\n',description ,'\n',organizer_name ,'\n',email ,'\n',phone ,'\n',capacity ,'\n',venue_name ,'\n',location )
            flag = 3

        if flag == 3:
            venue = Venue(Capacity = capacity, Venue_name = venue_name, Location = location)
            venue.save()
            Events = Event(Event_Name =event_name, Event_Duration = event_duration, Event_Date = event_date, Description = description, Venue_ID = venue )
            Events.save()
            org = Organiser(UserName = organizer_name, Email = email, Phone = phone)
            org.save()
            Com = Committee(Event_ID = Events, Org_ID = org)
            Com.save()

    return render(request, 'event_page.html')


def Reg_event(request):
    if request.method == 'POST':
        #form = EventRegistrationForm(request.POST)
        form_identifier = request.POST.get('form_identifier')
        if ('form1' in request.POST) or (form_identifier == 'form1'):
            attendee_name = request.POST.get('attendee_name')
            attendee_email = request.POST.get('attendee_email')
            attendee_phone = request.POST.get('attendee_phone')
            event_id = request.POST.get('event')
            Attend = Attendee(Attendee_Name = attendee_name, AttendeeEmail =attendee_email,AttendeePhone =attendee_phone)
            Attend.save()
            Ticket = Registration(Tickettype = "FULL", Event_ID = Event.objects.get(pk=event_id) ,Attendee_ID = Attend )
            Ticket.save()
            try:
                event = Event.objects.get(pk=event_id)
                registration_message = f'Registered for the event: {event.Event_Name}'
                return HttpResponse(registration_message)
            except Event.DoesNotExist:
                registration_message = 'Event not found'
                return HttpResponse(registration_message)
    else:
        events = Event.objects.all()
    events = Event.objects.all()
    return render(request, 'Reg_page.html', {'events': events})