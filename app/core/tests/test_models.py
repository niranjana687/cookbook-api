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
        user = get_user_model.objects.create_user(
            email, 
            'mathiBro'
            )
        
        self.assertEqual(user.email, email.lower())
    

         