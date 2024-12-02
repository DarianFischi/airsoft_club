from datetime import datetime, time
from django.urls import reverse
from django.test import TestCase
from .models import Event

class EventViewTests(TestCase):
    
    def test_create_event_valid_data(self):
        """
        Test case for valid form data when creating an event.
        """
        # Prepare valid data for the POST request
        data = {
            'title': 'Test Event',
            'description': 'This is a test event',
            'date': '2024-12-01',
            'time': '10:00:00',
            'location': 'Test Location',
        }

        # Send a POST request with the valid data to the 'create_event' URL
        response = self.client.post(reverse('create_event'), data)

        # verifying event was put into database
        self.assertEqual(Event.objects.count(), 1)
        
        if Event.objects.count() == 0:
            form = response.context.get('form')
            if form:
                # If form exists in the context, print form errors
                print("Form errors:", form.errors)
            else:
                print("No form found in context.")

        # putting the test event to verify data
        event = Event.objects.first()

        # validating all data
        self.assertEqual(event.title, 'Test Event')
        self.assertEqual(event.description, 'This is a test event')
        self.assertEqual(event.date, datetime(2024, 12, 1).date())
        # extra step needed to verify the time is in the correct format
        expected_time = time(10, 0)
        self.assertEqual(event.time, expected_time)
        self.assertEqual(event.location, 'Test Location')
        

    def test_create_event_no_title(self):
        """
        Test case for valid form data when creating an event.
        """
        # Prepare valid data for the POST request
        data = {
            'title': '',
            'description': 'This is a test event',
            'date': '2024-12-01',
            'time': '10:00:00',
            'location': 'Test Location',
        }

        # creating the event
        response = self.client.post(reverse('create_event'), data)
        
        #error checking
        if Event.objects.count() == 0:
            form = response.context.get('form')
            if form:
                print("Form errors:", form.errors)
            else:
                print("No form found in context.")

        # verifying event was put into database
        self.assertEqual(Event.objects.count(), 1)

    def test_create_event_no_description(self):
        """
        Test case for valid form data when creating an event.
        """
        # Prepare valid data for the POST request
        data = {
            'title': 'Test Event',
            'description': '',
            'date': '2024-12-01',
            'time': '10:00:00',
            'location': 'Test Location',
        }

        # creating the event
        response = self.client.post(reverse('create_event'), data)

        # verifying event was put into database
        self.assertEqual(Event.objects.count(), 1)
       
    def test_create_event_no_date(self):
        """
        Test case for valid form data when creating an event.
        """
        # Prepare valid data for the POST request
        data = {
            'title': 'Test Event',
            'description': 'This is a test event',
            'date': '',
            'time': '10:00:00',
            'location': 'Test Location',
        }

        # creating the event
        response = self.client.post(reverse('create_event'), data)

        #error checking
        if Event.objects.count() == 0:
            form = response.context.get('form')
            if form:
                print("Form errors:", form.errors)
            else:
                print("No form found in context.")
                
        # verifying event was put into database
        self.assertEqual(Event.objects.count(), 1)

        
    def test_create_event_no_time(self):
        """
        Test case for valid form data when creating an event.
        """
        # Prepare valid data for the POST request
        data = {
            'title': 'Test Event',
            'description': 'This is a test event',
            'date': '2024-12-01',
            'time': '',
            'location': 'Test Location',
        }

        # creating the event
        response = self.client.post(reverse('create_event'), data)

        #error checking
        if Event.objects.count() == 0:
            form = response.context.get('form')
            if form:
                print("Form errors:", form.errors)
            else:
                print("No form found in context.")
                
        # verifying event was put into database
        self.assertEqual(Event.objects.count(), 1)
        
    def test_create_event_no_location(self):
        """
        Test case for valid form data when creating an event.
        """
        # Prepare valid data for the POST request
        data = {
            'title': '',
            'description': 'This is a test event',
            'date': '2024-12-01',
            'time': '10:00:00',
            'location': '',
        }

        # creating the event
        response = self.client.post(reverse('create_event'), data)

        #error checking
        if Event.objects.count() == 0:
            form = response.context.get('form')
            if form:
                print("Form errors:", form.errors)
            else:
                print("No form found in context.")

        # verifying event was put into database
        self.assertEqual(Event.objects.count(), 1)
        
        
