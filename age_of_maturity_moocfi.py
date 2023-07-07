# Write your solution here
def ask_user():
    age = int(input("How old are you? "))
    return age

def check_age(age):
    if age >= 18:
        return True
    else:
        return False

def output(is_adult):
    if is_adult:
        print("You are of age!")
    else:
        print("You are not of age!")

def main():
    age = ask_user()
    is_adult = check_age(age)
    output(is_adult)

main()

