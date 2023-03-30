
def login_decor(func):

    def check(*args, **kwargs):
        login = input("Your login: ")
        password = input("Your password: ")
        if login == new_login and password == new_pass:
            func(*args, **kwargs)
        else:
            print("Wrong login or password!")
    return check


@login_decor
def logining():
    print("Here is your account!")


if __name__ == "__main__":
    new_login = "qwerty"
    new_pass = "123456"
    logining()
