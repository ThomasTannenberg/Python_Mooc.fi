def palindromes(word):
    return word == word[::-1]

while True:
    user_input = input("Please type in a palindrome: ")

    if palindromes(user_input):
        print(user_input + " is a palindrome!")
        break

    else:
        print("that wasn't a palindrome")

#if __name__ == "__main__":

