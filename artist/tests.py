from django.test import TestCase
from .models import Profile, Post, Comments
from django.contrib.auth.models import User

class TestProfile(TestCase):
    def setUp(self):
        self.user = User( username = 'Brian', email = 'g@gmail.com', password = 'beta')
        self.user.save()
        self.profile = Profile( name='Brian', profile_picture = 'test.jpeg',bio='this is a test bio', contact = 0, user=self.user, )
        
        
    def test_instance(self):
        self.assertTrue(isinstance(self.prfile, Profile))
        
    def save_profile(self):
        self.profile.save()
        
    def delete_profile(self):
        self.profile.delete()
        
        
