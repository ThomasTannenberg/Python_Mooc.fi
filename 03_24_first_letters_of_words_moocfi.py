# Write your solution here
def first_letters(words_list):


    for word in words_list:

        first_letter = word[0]
        print (first_letter)
          
    
def main():
    words_list = []
    user_input = input("Please type in a sentence: ")
    words_list = user_input.split()
    first_letters(words_list)

main()