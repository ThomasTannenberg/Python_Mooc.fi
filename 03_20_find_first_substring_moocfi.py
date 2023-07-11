# Write your solution here
def print_slice():
    word = input("Please type in a word: ")
    char = input("Please type in a character: ")

    index = word.find(char)  

    if index != -1 and len(word) - index >= 3:
        slice = word[index:index + 3]  
        print(slice)


print_slice()
