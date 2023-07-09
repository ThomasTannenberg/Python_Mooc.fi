from math import sqrt


def ask_user():
    number = int(input("Please type ina a number: "))
    return number

def check_number():
    while True:
        
        number = ask_user()

        if number < 0:
            print("Invalid number")
        elif number == 0:
            print("Exiting...")
            break
        else:
            print(sqrt(number))
        
def main():

    check_number()

main()
