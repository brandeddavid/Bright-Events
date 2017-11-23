class User(object):

    def __init__(self):

        self.users = {}

    def createUser(self, name, email, password):

        details = []

        if email in self.users.keys():

            print('Email already has an account')

        else:

            details.append(name)
            details.append(password)

            self.users[email] = details

            print ('Registration Successful')

        return self.users

    def login(self, email, password):

        if email == ' ' or password == ' ':

            return 'Fields Required'

        elif email in self.users.keys():

            if password == self.users[email][1]:

                return 'Login Successful'
            else:

                return 'Password do not match'

        return 'You have not signed up for an account'

class Event(object):

    def __init__(self):

        self.events = {}

    def createEvent(self, id, name, category, location, date, time, description):

        eventdetails = []

        eventdetails.append(name)
        eventdetails.append(category)
        eventdetails.append(date)
        eventdetails.append(time)
        eventdetails.append(description)

        self.events[id] = eventdetails

        return 'Event added'

    def deleteEvent(self, id):

        if id in self.events.keys():

            del(self.events[id])

        return 'Event Deleted'

    def updateEvent(self, id, name, category, location, date, time,description):

        if id in self.events.keys():

            self.events[id][0] = name
            self.events[id][1] = category
            self.events[id][2] = location
            self.events[id][3] = date
            self.events[id][4] = time
            self.events[id][5] = description

        return 'Update Successful'

    def searchCategory(self, category):

        for id in self.events.keys():

            if self.events[id][2] == category:

                return self.events[id]

    def searchLocation(self, location):

        for id in self.events.keys():

            if self.events[id][3] == location:

                return self.events[id]
