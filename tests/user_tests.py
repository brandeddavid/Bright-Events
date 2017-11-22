import unittest

from app import models

class Testcreateuser(unittest.TestCase):

    """ Class for testing user creation"""

    def setUp(self):

        self.user = models.User()


    def test_user_registration_success(self):

        result = self.user.createUser('dmwangi','dmwangi@gmail.com','dmwangi','dmwangi')

        self.assertEqual(result, 'Registration Successful')
