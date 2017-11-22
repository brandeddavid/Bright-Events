class User(object):

    def __init__(self):

        self.users = {}

    def createUser(self, name, email, password, confirmpassword):

        details = []

        if email in self.users.keys():

            return 'Email already has an account'

        else:

            if password == confirmpassword:

                details.append(name,password,confirmpassword)

                self.users[email] = details

            else:

                return "Passwords do not match"

        return 'Registration Successful'

    def login(self, email, password):

        if email in self.users.keys():

            if password == self.users[email][1]:

                return 'Login Successful'
            else:

                return 'Password do not match'

        return 'You have not signed up for an account'
