from django.shortcuts import render, redirect, get_object_or_404
from .models import Event
from .forms import EventForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from datetime import datetime, timedelta

# List of eventi
@login_required
def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})

# Event creation
@login_required
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
  
# Event Edit  
@login_required
def edit_event(request, event_id):
    # Fetch the event to edit
    event = get_object_or_404(Event, id=event_id)
    
    # Check if the event is being edited by its creator (optional, you can add your own logic here)
    #if event.created_by != request.user:
    #    return redirect('event_list')  # Redirect if the user is not the creator of the event
    
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)  # Bind form with the existing event data
        if form.is_valid():
            form.save()  # Save the edited event
            return redirect('event_list')  # Redirect to the event list page after saving
    else:
        form = EventForm(instance=event)  # Pre-fill the form with the event's current data
    
    return render(request, 'events/edit_event.html', {'form': form, 'event': event})
  
# Event deletion
@login_required
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

# @login_required
def get_events(request):
    # Get all events from the database
    events = Event.objects.all()

    events_data = []
    for event in events:
        # Combine the event's date and time to create the start datetime
        start_datetime = datetime.combine(event.date, event.time)

        # For simplicity, set the end time to be 1 hour after the start time (if no end time is provided)
        # You can adjust this duration based on your requirements
        end_datetime = start_datetime + timedelta(hours=6)

        events_data.append({
            'id': event.id,
            'description': event.description or "No description available.",
            'title': event.title,
            'start': start_datetime.isoformat(),  # Ensure start is in ISO 8601 format
            'end': end_datetime.isoformat(),      # Ensure end is in ISO 8601 format
        })

    # Return the events data in JSON format for FullCalendar
    return JsonResponse(events_data, safe=False)
