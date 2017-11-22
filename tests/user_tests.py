import unittest

from app import models

class Testcreateuser(unittest.TestCase):

    """ Class for testing user creation"""

    def setUp(self):

        self.user = models.User()


    def test_user_registration_success(self):

        result = self.user.createUser('dmwangi','dmwangi@gmail.com','dmwangi','dmwangi')

        self.assertEqual(result, 'Registration Successful')

    def test_user_user_already_exists(self):

        self.user.createUser('dmwangi','dmwangi@gmail.com','dmwangi','dmwangi')

        result = self.user.createUser('dmwangi','dmwangi@gmail.com','dmwangi','dmwangi')

        self.assertEqual(result, 'Email already has an account')
