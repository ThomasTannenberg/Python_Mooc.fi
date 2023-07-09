# Write your solution here
def check_ln(string1, string2):
    if len(string1) > len(string2):
        return (string1 + " is longer")
    elif len(string2) > len(string1):
        return (string2 + " is longer")
    else:
        return ("The strings are equally long")
    


def main():
    string1 = input("Please type in string1: ")
    string2 = input("Please type in string2: ")
    output = check_ln(string1, string2)
    print(output)

main()