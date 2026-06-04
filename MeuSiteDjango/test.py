from django.test import TestCase
from django.contrib.auth.models import User

class LoginTest(TestCase):
    def setUp(self):
        User.objects.create_user(username='teste', password='12345678')

    def test_login(self):
        self.client.get('/login/')