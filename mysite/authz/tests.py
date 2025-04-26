from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages

class LoginViewTests(TestCase):
        
    def test_unsuccessful_login(self):
        """
        Test that the login page shows an error with incorrect credentials.
        """
        response = self.client.post(reverse('login'), {'username': 'wronguser', 'password': 'wrongpassword'})
        self.assertContains(response, "Please enter a correct username and password.")

class RegisterViewTests(TestCase):

    def test_successful_registration(self):
        """
        Test that a user can successfully register.
        """
        data = {
            'first_name': 'Test',
            'last_name': 'User',
            'username': 'newuser',
            'password': 'newpassword123',
            'password2': 'newpassword123'
        }
        
        # Send POST request to register endpoint
        response = self.client.post(reverse('register'), data)
        
        # Check that the user is redirected to the registration page after successful registration
        # Since you're redirecting to '/register/', check for a redirect status (302)
        self.assertRedirects(response, '/register/')
        
        # Check that a new user has been created
        self.assertTrue(User.objects.filter(username='newuser').exists())
        
        # Check that the correct success message is in the session (not in the response HTML)
        # Redirects don’t carry the messages, so check the session messages instead
        messages_list = list(response.wsgi_request._messages)
        self.assertTrue(any(message.message == "Account created Successfully!" for message in messages_list))

    def test_password_validation_failure(self):
        """
        Test that the registration page shows an error when password validation fails.
        """
        data = {
            'first_name': 'Test',
            'last_name': 'User',
            'username': 'newuser',
            'password': 'short',  # A short password to trigger validation failure
            'password2': 'short'
        }

        # Send POST request with invalid password
        response = self.client.post(reverse('register'), data)

        # Check that the response status is 400 (because it's a validation error)
        self.assertEqual(response.status_code, 400)

        # Check if the error message is in the JSON response body
        json_response = response.json()  # Parse the JSON response
        self.assertIn('This password is too short. It must contain at least 8 characters.', json_response['errors'])
       

    def test_password_mismatch(self):
        """
        Test that the registration page shows an error when the passwords don't match.
        """
        data = {
            'first_name': 'Test',
            'last_name': 'User',
            'username': 'newuser',
            'password': 'newpassword123',
            'password2': 'differentpassword123'  # Password mismatch
        }

        # Send POST request with mismatched passwords
        response = self.client.post(reverse('register'), data)

        # Check that the response status is 302 (redirect)
        self.assertEqual(response.status_code, 302)

        # Follow the redirect to the /register/ page
        response = self.client.get(response.url)

        # Check that the page contains the "Passwords Don't Match" error message
        self.assertContains(response, "Passwords Don&#x27;t Match")

