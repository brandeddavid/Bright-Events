import unittest

from app import models

class Testcreateuser(unittest.TestCase):

    """ Class for testing user creation model"""

    def setUp(self):

        """Instance of class user"""

        self.user = models.User()


    def test_user_registration_success(self):

        """Test for successful user registration"""

        result = self.user.createUser('dmwangi','dmwangi@gmail.com','dmwangi','dmwangi')

        self.assertEqual(result, 'Registration Successful')

    def test_user_already_exists(self):

        """Tests for already existing users"""

        self.user.createUser('dmwangi','dmwangi@gmail.com','dmwangi','dmwangi')

        result = self.user.createUser('dmwangi','dmwangi@gmail.com','dmwangi','dmwangi')

        self.assertEqual(result, 'Email already has an account')

    def test_user_password_mismatch(self):

        """Tests for missmatched password"""

        result = self.user.createUser('dmwangi','dmwangi@gmail.com','dmwangi','notme')

        self.assertEqual(result, 'Passwords do not match')

    def test_missing_email(self):

        """Tests for missing email address"""

        result = self.user.createUser('dmwangi',' ','dmwangi','dmwangi')

        self.assertEqual(result, 'Fields Required')

class Testloginuser(unittest.TestCase):

    """Tests user login method"""

    def setUp(self):

        """Instance of user class"""

        self.user = models.User()

    def test_user_login_success(self):

        """Tests Successful  user login"""

        self.user.createUser('dmwangi','dmwangi@gmail.com','dmwangi','dmwangi')

        result = self.user.login('dmwangi@gmail.com','dmwangi')

        self.assertEqual(result, 'Login Successful')

    def test_user_password_mismatch(self):

        """Tests password mismatch during login"""

        self.user.createUser('dmwangi','dmwangi@gmail.com','dmwangi','dmwangi')

        result = self.user.login('dmwangi@gmail.com','wrongpas')

        self.assertEqual(result, 'Password do not match')

    def test_user_not_signedup(self):

        """Tests for user not signed up"""

        self.user.createUser('dmwangi','dmwangi@gmail.com','dmwangi','dmwangi')

        result = self.user.login('dkinuthia@gmail.com','dunkin')

        self.assertEqual(result, 'You have not signed up for an account')


if __name__ == '__main__':
    unittest.main()
