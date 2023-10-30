from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_management, name='event_management'),
    path('Register', views.Reg_event, name = 'Reg_event'),
]
