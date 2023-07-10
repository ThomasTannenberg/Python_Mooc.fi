def print_substrings(word):
    index = 0
    for n in range (0, len(word)):
        index += 1
        print(word[0:index])


def main():
    word = input("Please type in a string: ")
    print_substrings(word)

main()