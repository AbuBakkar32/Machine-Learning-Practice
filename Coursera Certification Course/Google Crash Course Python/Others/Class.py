class User:
    name = ''
    email = ''
    password = ''
    login = False

    def __init__(self, name, email, password):  # Constructor class
        self.name = name
        self.email = email
        self.password = password

    def login(self):
        email = input('Enter email: ')
        password = input('Enter Password: ')

        if email == self.email and password == self.password:
            login = True
            print("Login Successful")
        else:
            print('Login Failed')

    def logout(self):
        login = False
        print("Logout Successfully")

    def isLoggedIn(self):
        if self.login:
            return True
        else:
            return False

    def profile(self):
        if self.isLoggedIn():
            print(self.name, '\n', self.email)
        else:
            print("User is not Logged in!!!")


user1 = User('Rakib', 'rakib@gmail.com', '12345')
user1.login()

