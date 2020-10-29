from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def sample_user(email='sample_user@test.com', password='testpass123'):
    """Create sample user"""
    return get_user_model().object.create_user(email, password)


class ModelTest(TestCase):

    def test_create_user_with_email(self):
        """Test if creating a new user with email is successful"""
        email = "test@gmail.com"
        password = 'TEST1234test'
        user = get_user_model().object.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalize(self):
        """""Test if the email for a new user is normalize"""
        email = 'test@LOWERCASE.COM'
        user = get_user_model().object.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test if creating a user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().object.create_user(None, 'test123')

    def test_create_super_user(self):
        """Test if creating a superuser is successful"""
        user = get_user_model().object.create_superuser(
            'superuser@test.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """Test the tag string representation"""
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='vegan'
        )

        self.assertEqual(str(tag), tag.name)

    def test_ingredient_str(self):
        """Test the ingredient string representation"""
        ingredient = models.Ingredient.objects.create(
            user=sample_user(),
            name='Cucumber'
        )

        self.assertEqual(str(ingredient), ingredient.name)
