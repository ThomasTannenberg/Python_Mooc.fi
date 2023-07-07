# Write your solution here


def output(length, word):
    if length > 1:
        print("There are", length, "letters in the word", word)
        print("Thank you!")
    else:
        print("Thank you!")


def check_length(word):
    length = len(word)
    return length

def ask_user():
    word = input("Please type in a word: ")
    return word

def main():
    word = ask_user()
    length = check_length(word)
    output(length, word)

main()

