# Write your solution here
def user_input():
    word1 = input("Please type in the 1st word: ")
    word2 = input("Please type in the 2nd word: ")
    return word1, word2

def check_words(word1, word2):
    return_word =""

    if word1 > word2:
        return_word = word1
        return return_word
    
    elif word2 > word1:
        return_word = word2
        return return_word
    
    else:
        return_word is None

def output(return_word):
    if return_word is None:
        print("You gave the same word twice.")
    else:
        print(return_word, "comes alphabetically last.")

def main():
    word1, word2 = user_input()
    return_word = check_words(word1, word2)
    output(return_word)

main()


