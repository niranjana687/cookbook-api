from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models

class ModelTests(TestCase):

    def test_create_user_with_mail_successful(self):
        """Test creating user with email is successful"""
        email="niranjana687@gmail.com"
        password="itsOkayBruh"
        user= get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    
    def test_new_user_email_normalised(self):
        """"Test checking if email for new user is normalised"""
        email = "niranjana@GMAIL.COM"
        user = get_user_model().objects.create_user(
            email, 
            'mathiBro'
            )
        
        self.assertEqual(user.email, email.lower())
    
    def test_new_user_invalid_mail(self):
        """Test checking if mail of new user is invalid"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_superuser(self):
        """Test checking if new user is super user"""
        user = get_user_model().objects().create_user(
            'niranjana687@gmail.com',
            'pleaseWorkBro'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)


         