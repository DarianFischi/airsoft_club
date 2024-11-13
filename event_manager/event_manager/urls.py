from django.contrib import admin  # Import the admin module
from django.urls import path, include  # Ensure you import include to reference other app's URLs
from events import views  # Import your views if necessary

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin URL route
    path('events/', include('events.urls')),  # If your event-related URLs are in the events app
    path('calendar/events/', views.get_events, name='get_events'),  # Your events JSON API endpoint
]
