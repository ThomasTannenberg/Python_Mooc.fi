


def ask_input():
    number1 = int(input("Please give a number:"))
    number2 = int(input("Please give a second number:"))
    operation = input("What operation would you like to do? [add, multiply or substract]?")
    return number1, number2, operation

def ask_operation(number1, number2, operation):
    if operation == "substract":
        result = number1 - number2
    elif operation == "add":
        result = number1 + number 2
    elif operation == "multiply":
        result = number1 * number2
    else:
        result = "none"

    return result

def output(number1, number2, operation, result):
    if operation == "substract":
        print(number1, "-", number2, "=", result)
    elif operation == "add":
        print(number1, "+", number2, "=", result)
    elif operation == "multiply":
        print(number1, "*", number2, "=", result)

def main():
    number1, number2, operation = ask_input()
    result = ask_operation(number1, number2, operation)
    output(number1, number2, operation, result)

main()






