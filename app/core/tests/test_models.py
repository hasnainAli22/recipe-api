"""
Test for models
"""
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Test Models"""

    def test_create_user_with_email(self):
        """Test creating user with email successful"""
        email = 'test@example.com'
        password = 'testpassword'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))


    def test_new_user_email_normalized(self):
        """Checking if the email is normalized or not"""
        sample_emails = [
            ['test1@EXAMPLE.com','test1@example.com'],
            ['Test2@example.com','Test2@example.com'],
            ['TEST3@example.com','TEST3@example.com'],
            ['TEST4@example.COM','TEST4@example.com']
        ]
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, password='test123')
            self.assertEqual(user.email, expected)


    def test_raise_error_if_not_provided_email(self):
        """Raise Error if email is not provided"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('','pass123')


    def test_create_superuser(self):
        """Test creating a super user"""
        user = get_user_model().objects.create_superuser(
            'test@example.com',
            'test123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
    
