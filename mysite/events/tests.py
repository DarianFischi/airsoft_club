from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Event
from datetime import datetime

class EventViewTests(TestCase):
    # Setup method to create a user for authentication
    def setUp(self):
        # Create a user to test login functionality
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Optionally create a test event for later tests
        self.event = Event.objects.create(
            title='Test Event',
            description='This is a test event',
            date=datetime(2024, 12, 1),
            time=datetime(2024, 12, 1, 10, 0),
            location='Test Location',
            created_by=self.user
        )

    # Test case for accessing event list as a logged-in user
    def test_event_list_authenticated(self):
        self.client.login(username='testuser', password='testpassword')  # Login user
        response = self.client.get(reverse('event_list'))  # Access event list
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'events/event_list.html')
        self.assertContains(response, 'Test Event')  # Ensure the test event is in the list

    # Test case for trying to access event list without login
    def test_event_list_not_authenticated(self):
        response = self.client.get(reverse('event_list'))  # Access event list without login
        self.assertRedirects(response, '/accounts/login/?next=/events/')  # Should redirect to login

    # Test case for creating an event (authenticated)
    def test_create_event_authenticated(self):
        self.client.login(username='testuser', password='testpassword')  # Login user
        data = {
            'title': 'New Test Event',
            'description': 'Test Description for new event',
            'date': '2024-12-02',
            'time': '15:00:00',
            'location': 'New Test Location'
        }
        response = self.client.post(reverse('create_event'), data)  # Submit POST request to create event
        self.assertRedirects(response, reverse('event_list'))  # After creation, it should redirect to event list
        self.assertEqual(Event.objects.count(), 2)  # Ensure the event count is now 2 (1 existing + 1 created)

    # Test case for trying to create an event without login
    def test_create_event_not_authenticated(self):
        data = {
            'title': 'Unauthenticated Event',
            'description': 'This event should not be created without login',
            'date': '2024-12-02',
            'time': '17:00:00',
            'location': 'Unauthenticated Location'
        }
        response = self.client.post(reverse('create_event'), data)  # Attempt to create event without login
        self.assertRedirects(response, '/accounts/login/?next=/events/create/')  # Should redirect to login

    # Test case for editing an event (authenticated)
    def test_edit_event_authenticated(self):
        self.client.login(username='testuser', password='testpassword')  # Login user
        event = self.event  # Use the event created in setUp
        data = {
            'title': 'Updated Test Event',
            'description': 'Updated description for the event',
            'date': '2024-12-01',
            'time': '12:00:00',
            'location': 'Updated Location'
        }
        response = self.client.post(reverse('edit_event', kwargs={'event_id': event.id}), data)  # POST request to edit
        self.assertRedirects(response, reverse('event_list'))  # Redirect to event list after edit
        event.refresh_from_db()  # Refresh the event from the database to check the changes
        self.assertEqual(event.title, 'Updated Test Event')  # Ensure the title was updated
        self.assertEqual(event.description, 'Updated description for the event')  # Ensure the description was updated

    # Test case for deleting an event (authenticated)
    def test_delete_event_authenticated(self):
        self.client.login(username='testuser', password='testpassword')  # Login user
        event = self.event  # Use the event created in setUp
        response = self.client.post(reverse('delete_event', kwargs={'event_id': event.id}))  # POST request to delete
        self.assertRedirects(response, reverse('event_list'))  # Redirect to event list after deletion
        self.assertEqual(Event.objects.count(), 0)  # Ensure the event was deleted

    # Test case for trying to delete an event without login
    def test_delete_event_not_authenticated(self):
        response = self.client.post(reverse('delete_event', kwargs={'event_id': self.event.id}))  # Attempt delete without login
        self.assertRedirects(response, '/accounts/login/?next=/events/event/{}/delete/'.format(self.event.id))  # Redirect to login

        
   
