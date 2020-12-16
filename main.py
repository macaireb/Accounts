# generic library to run an account, with the intention of linking with a
# sqlite db

def setpassword():
    password = input("password: ")
    return password


def setusername():
    userName = input("username: ")
    return userName


class account:
    user = dict()

    def getpass(self, username):
        return self.user[username]

    def __init__(self):
        UserName = setusername()
        Password = setpassword()
        self.user[UserName] = Password


newUser = account()
print(newUser.getpass("macaire"))