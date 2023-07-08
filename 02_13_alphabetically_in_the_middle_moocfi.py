# Write your solution here

def check_middle(letter1, letter2, letter3):
    if letter1 < letter2 < letter3 or letter3 < letter2 < letter1:
        middle_letter = letter2

    elif letter2 < letter1 < letter3 or letter3 < letter1 < letter2:
        middle_letter = letter1
    
    else:
        middle_letter = letter3
    
    return middle_letter

def output(middle_letter):
    print("The letter in the middle is", middle_letter)



def main():
    letter1 = input("1st letter: ")
    letter2 = input("2nd letter: ")
    letter3 = input("3rd letter: ")

    middle_letter = check_middle(letter1, letter2, letter3)

    output(middle_letter)

main()

