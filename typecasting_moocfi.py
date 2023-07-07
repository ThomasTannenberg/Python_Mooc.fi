# Write your solution here

def ask_user():
    float_number = float(input("Please type in a number: "))
    return float_number

def conversion(float):
    int_number = int(float)
    remainder = float - int_number
    return int_number, remainder

def output(int_number, remainder):
    print("Integer part: ", int_number)
    print("Decimal part: ", remainder)

def main():
    float = ask_user()
    int_number, remainder = conversion(float)
    output(int_number, remainder)

main()


