from django.urls import path
from .views import event_list, create_event, delete_event, calendar_view, get_events

urlpatterns = [
    # Existing event list page
    path('', event_list, name='event_list'),
    
    # Event creation page
    path('create/', create_event, name='create_event'),
    
    # Event deletion page
    path('event/<int:event_id>/delete/', delete_event, name='delete_event'),
    
    # New calendar page
    path('calendar/', calendar_view, name='calendar'),
    
    # Endpoint for fetching events data (used by FullCalendar)
    path('calendar/events/', get_events, name='get_events'),
]
