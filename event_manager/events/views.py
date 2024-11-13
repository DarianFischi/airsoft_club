from django.shortcuts import render, redirect, get_object_or_404
from .models import Event
from .forms import EventForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from datetime import datetime

# List of events
def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})

# Event creation
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.created_by = None  # Set to None or your user logic
            event.save()
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'events/create_event.html', {'form': form})

# Event deletion
def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        event.delete()
        return redirect('event_list')
    return render(request, 'events/delete_event_confirm.html', {'event': event})

# New calendar view
def calendar_view(request):
    # This will render the main calendar page
    return render(request, 'events/calendar.html')

# Fetch events data for the calendar (AJAX)
def get_events(request):
    # Get all events from the database
    events = Event.objects.all()

    # Prepare the events data for FullCalendar
    events_data = []
    for event in events:
        # Combine date and time to create the start datetime (using the event's date and time)
        start_datetime = datetime.combine(event.date, event.time)
        end_datetime = start_datetime  # Assuming events have no end time, otherwise add logic for 'end_time'
        
        events_data.append({
            'id': event.id,
            'title': event.title,
            'start': start_datetime.isoformat(),  # Format the datetime for FullCalendar
            'end': end_datetime.isoformat(),      # For simplicity, we use the same time as end time
        })
    
    # Return the events in JSON format to be used by FullCalendar
    return JsonResponse(events_data, safe=False)
