# events/admin.py
from django.contrib import admin
from .models import Event, Committee, Organiser, Venue, Registration, Attendee

admin.site.register(Venue)
admin.site.register(Event)
admin.site.register(Organiser)
admin.site.register(Committee)
admin.site.register(Attendee)
admin.site.register(Registration)


