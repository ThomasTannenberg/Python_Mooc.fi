# Write your solution here

def check_characters(word):
    if word[1] == word[-2]:
        return True
    else:
        return False

def output(is_same, word):
    if is_same:
        print("The second and the second to last characters are", word[1])
    else:
        print("The second and the second to last characters are different")

       
def main():
    word = input("Please type in a string: ")
    is_same = check_characters(word)
    output(is_same, word)


main()
    