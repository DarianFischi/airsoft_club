from datetime import datetime
from django.urls import reverse
from django.test import TestCase
from .models import Event

class EventViewTests(TestCase):

    def test_create_event_no_title(self):
        """
        Test case for valid form data when creating an event without title.
        """
        # Prepare invalid data for the POST request
        data = {
            'title': '',  # Missing title
            'description': 'This is a test event',
            'date': '2024-12-01',
            'time': '10:00:00',
            'location': 'Test Location',
        }

        # Send a POST request
        response = self.client.post(reverse('create_event'), data)

        # If the form is valid, it will redirect, so check for the response code first.
        if response.status_code == 302:  # Redirection on valid form submission
            # Follow the redirect to the event list page
            response = self.client.get(response.url)

        # Now that we are on the 'create_event' page again, let's check for the form in context
        form = response.context.get('form')

        # If the form is returned in context, print any form errors.
        if form:
            print("Form errors:", form.errors)
        else:
            print("No form found in context.")

        # Check if the event count hasn't changed (because event creation should fail)
        self.assertEqual(Event.objects.count(), 0)

