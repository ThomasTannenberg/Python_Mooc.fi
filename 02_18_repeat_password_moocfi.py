def ask_user_password():
    password = input("Password: ")
    return password

def user_repeat_password():
    repeat_password = input("Repeat password: ")
    return repeat_password

def check_password():
    password = ask_user_password()

    while True:
        repeat_password = user_repeat_password()

        if repeat_password == password:
            print("User account created!")
            break
        else:
            print("They do not match!")

def main():
    check_password()

main()

