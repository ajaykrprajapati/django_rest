from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is isuccessful"""
        email = 'test@gmail.com'
        password = 'admin@123'
        user = get_user_model().object.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test creating a new user with an new email is normalised"""
        email = 'test@GMAIL.COM'
        user = get_user_model().object.create_user(
            email=email,
            password='admin@123'
        )

        self.assertEqual(user.email, email.lower())
        self.assertTrue(user.check_password('admin@123'))

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().object.create_user(None, "jfhfh")

    def test_create_new_superuser(self):
        """Test creating user with no email raises error"""
        user = get_user_model().object.create_superuser(
            'shdjhd@fjd.com', 'dgsf'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)