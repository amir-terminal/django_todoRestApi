from django.test import TestCase
from rest_framework.test import APITestCase
from authentification.models import User
# Create your tests here.


class TestModel(APITestCase):
    def test_createuser(self):
        user = User.objects.create_user('amirchehih','chehih.amir@hotmail.com','8302D10C0C')
        self.assertIsInstance(user,User)
        self.assertIsNotNone(user.username,'The given username must be set')
        self.assertIsNotNone(user.email,'The given email must be set')
        self.assertEqual(user.username,'amirchehih')
        self.assertEqual(user.email,'chehih.amir@hotmail.com')
        self.assertFalse(user.is_staff)
    def test_create_superuser(self):
        user = User.objects.create_superuser('amirchehih','chehih.amir@hotmail.com','8302D10C0C')
        self.assertIsInstance(user,User)
        self.assertEqual(user.username,'amirchehih')
        self.assertEqual(user.email,'chehih.amir@hotmail.com')
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
        
    
    def test_raise_error_when_username_not_supplied(self):
        self.assertRaises(ValueError,User.objects.create_user,username='',email="chehih.amir@hotmail.com",password='8302D10C0C')
        
    
    def test_raise_error_when_email_not_supplied(self):
        self.assertRaises(ValueError,User.objects.create_user,username='amirchehih',email="",password='8302D10C0C')
    
    def test_raises_error_when_isnot_superuser(self):
        self.assertRaises(ValueError,User.objects.create_superuser,username='amirchehih',email="chehih.amir@hotmail.com",password='8302D10C0C',is_superuser = False)
    
    def test_raises_error_when_isnot_staff(self):
        self.assertRaises(ValueError,User.objects.create_superuser,username='amirchehih',email="chehih.amir@hotmail.com",password='8302D10C0C',is_staff = False)
    