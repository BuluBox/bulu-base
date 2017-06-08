import mock

from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse


class LoginLogoutTestCase(TestCase):

    def setUp(self):
        self.username = 'test@bulubox.com'
        self.password = 'testtest'
        self.user = get_user_model().objects.create_user(
            username=self.username,
            password=self.password,
        )
        self.client = Client()

    def test_login(self):
        url = reverse('login')
        data = {
            'username': self.username,
            'password': self.password,
        }
        response = self.client.post(url, data)
        self.assertRedirects(response, reverse('index'))

    def test_login_next(self):
        next_url = '/login/'
        url = reverse('login') + '?next=' + next_url
        data = {
            'username': self.username,
            'password': self.password,
        }
        response = self.client.post(url, data)
        self.assertRedirects(response, next_url)

    @mock.patch('django.contrib.messages.info')
    @mock.patch('bulu.authentication.views.logout')
    def test_logout(self, logout_mock, info_mock):
        self.client.force_login(self.user)
        url = reverse('logout')
        response = self.client.get(url)
        self.assertRedirects(response, reverse('login'))
        self.assertTrue(logout_mock.called_once)
        self.assertTrue(info_mock.called_once)
