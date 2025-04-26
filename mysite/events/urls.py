from django.urls import path
from .views import event_list, create_event, edit_event, delete_event, calendar_view, get_events, upcoming_list, past_list

urlpatterns = [
    # Existing event list page
    path('', event_list, name='event_list'),

    # Upcoming event list
    path('upcoming_event_list/', upcoming_list, name='upcoming_list'),

    # Past event list
    path('past_event_list/', past_list, name='past_list'),

    # Event creation page
    path('create/', create_event, name='create_event'),

    # Event edit page
    path('edit/<int:event_id>/', edit_event, name='edit_event'),

    # Event deletion page
    path('event/<int:event_id>/delete/', delete_event, name='delete_event'),

    # New calendar page
    path('calendar/', calendar_view, name='calendar'),

    # Endpoint for fetching events data (used by FullCalendar)
    path('calendar/events/', get_events, name='get_events'),


]
