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

                return "Passwords don't match"

        return 'Registration Successful'
