from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

class TestingProfiles(TestCase):

    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='test_user', password='test_password')
    
    def test_profile(self):
        """
        Test if testuser can access profile
        """
        # Log the user in
        login = self.client.login(username='test_user', password='test_password')
        self.assertTrue(login)  # Ensure the user is logged in

        # Access the profile page
        response = self.client.get(reverse('profile'))  # Use 'reverse' to resolve the URL
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')

    def test_profile_logged_out(self):
        """
        Test if logged out user gets redirected
        when trying to access profile link
        """
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 302)