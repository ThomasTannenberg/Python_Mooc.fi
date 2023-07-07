# Write your solution here
def ask_user():
    number1 = int(input("Please type in the first number: "))
    number2 = int(input("Please type in the second number: "))
    return number1, number2

def check_numbers(number1, number2):
    number_return = int()
    if number1 > number2:
        number_return = number1
        return number_return
    if number2 > number1:
        number_return = number2
        return number_return
    else:
       return None
        
def output(number_return):
    if number_return is None:
        print("The numbers are equal!")
    else:
        print("The greater number was: ", number_return)

def main():
    number1, number2 = ask_user()
    number_return = check_numbers(number1, number2)
    output(number_return)

main()


