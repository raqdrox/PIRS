from django.test import TestCase
from django.urls import reverse, resolve
from .models import Profile
from .views import ProfileView, ProfileUpdateView
from django.contrib.auth import get_user_model

user = get_user_model()

class ProfileTest(TestCase):
    def setUp(self):
        self.user = user.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.profile = Profile.objects.create(
            user=self.user,
            name='test name',
            location='test location'
        )
        self.client.login(username='testuser', password='testpassword')

    def test_profile_view(self):
        url = reverse('user-profile')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'userprofile/profile.html')
        self.assertContains(response, 'test name')
        self.assertContains(response, 'test location')
        self.assertContains(response, 'testuser')
        self.assertNotContains(response, 'test password')
        
    def test_profile_update_view(self):
        url = reverse('user-profile-update')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'userprofile/profile_update.html')
        self.assertContains(response, 'test name')
        self.assertContains(response, 'test location')
        self.assertContains(response, 'testuser')
        self.assertNotContains(response, 'test password')

    def test_profile_url_resolves_profile_view(self):
        view = resolve('/profile/view/')
        self.assertEqual(view.func.__name__, ProfileView.as_view().__name__)

    def test_profile_url_resolves_profile_update_view(self):
        view = resolve('/profile/update/')
        self.assertEqual(view.func.__name__, ProfileUpdateView.as_view().__name__)

    def test_profile_model(self):
        self.assertEqual(self.profile.name, 'test name')
        self.assertEqual(self.profile.location, 'test location')
        self.assertEqual(self.profile.user, self.user)





