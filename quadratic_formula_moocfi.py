from math import sqrt

def use_sqrt(number_a, number_b, number_c):
    result1 = float((-number_b + sqrt(number_b**2 - 4 * number_a * number_c))) / (2 * number_a)
    result2 = float((-number_b - sqrt(number_b**2 - 4 * number_a * number_c))) / (2 * number_a)
    

    return result1, result2
    

def ask_user():
    number_a = int(input("Value of a: "))
    number_b = int(input("Value of b: "))
    number_c = int(input("Value of c: "))

    return number_a, number_b, number_c

def output(sqrt1, sqrt2):
    print("The roots are", sqrt1, "and", sqrt2)


def main():
    number_a, number_b, number_c = ask_user()
    sqrt1, sqrt2 = use_sqrt(number_a, number_b, number_c)
    output(sqrt1, sqrt2)

main()




