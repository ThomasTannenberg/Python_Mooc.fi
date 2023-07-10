def user_input():
    user_string = input("Please type in a string: ")
    return user_string

def output_underlining():
    while True:
        user_string = user_input()

        if user_string == "":
            break
        else:
            print(user_string)
            print("-" * len(user_string))


def main():
    output_underlining()

main()