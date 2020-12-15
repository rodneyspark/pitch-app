import unittest
from app.models import Pitch, User
from flask_login import current_user
from app import db

class PitchTest(unittest.TestCase):
    
    """
    Test class to test the behaviour of the Pitch
    """
    def setUp(self):
    
        """
        Set up method that will run before every Test
        """
        self.user_Ringer = User(username = 'rodneygakuru@gmail.com',password = 'rodgaks2000')
        self.new_pitch = Pitch(title= 'Looking for a Job', post = 'text', category = 'job')
    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch))
        