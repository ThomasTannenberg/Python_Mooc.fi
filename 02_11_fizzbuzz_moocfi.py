# Write your solution here


def divisible(number):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0:
        print("Fizz")

def main():
    number = int(input("Number: "))
    divisible(number)

main()
