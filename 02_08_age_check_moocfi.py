def check_age(age):
    if age >= 5 and age > 0:
        print("Ok, you're", age, "years old")
    elif age < 0:
        print("That must be a mistake")
    else:
        print("I suspect you can't write quite yet...")

def main():
    age = int(input("What is your age? "))
    check_age(age)

main()



