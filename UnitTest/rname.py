class Rname:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def getFullName(self):
        return self.firstName.lower() + ' ' + self.lastName.lower()

