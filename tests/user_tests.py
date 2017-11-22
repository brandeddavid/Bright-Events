import unittest

from app import models

class Testcreateuser(unittest.TestCase):

    """ Class for testing user creation"""

    def setUp(self):

        self.user = models.User()


    def test_user_registration_success(self):

        result = self.user.createUser('dmwangi','dmwangi@gmail.com','dmwangi','dmwangi')

        self.assertEqual(result, 'Registration Successful')

    def test_user_already_exists(self):

        self.user.createUser('dmwangi','dmwangi@gmail.com','dmwangi','dmwangi')

        result = self.user.createUser('dmwangi','dmwangi@gmail.com','dmwangi','dmwangi')

        self.assertEqual(result, 'Email already has an account')

    def test_user_password_mismatch(self):

        result = self.user.createUser('dmwangi','dmwangi@gmail.com','dmwangi','notme')

        self.assertEqual(result, 'Passwords do not match')

class Testloginuser(unittest.TestCase):

    def setUp(self):

        self.user = models.User()

    def test_user_login_success(self):

        self.user.createUser('dmwangi','dmwangi@gmail.com','dmwangi','dmwangi')

        result = self.user.login('dmwangi@gmail.com','dmwangi')

        self.assertEqual(result, 'Login Successful')

    def test_user_password_mismatch(self):

        self.user.createUser('dmwangi','dmwangi@gmail.com','dmwangi','dmwangi')

        result = self.user.login('dmwangi@gmail.com','wrongpas')

        self.assertEqual(result, 'Password do not match')

    def test_user_not_signedup(self):

        self.user.createUser('dmwangi','dmwangi@gmail.com','dmwangi','dmwangi')

        result = self.user.login('dkinuthia@gmail.com','dunkin')

        self.assertEqual(result, 'You have not signed up for an account')
