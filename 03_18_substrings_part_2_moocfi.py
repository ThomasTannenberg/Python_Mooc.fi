def print_substrings(word):

    for i in range(1, len(word) + 1):
        substring = word[-i:]
        print(substring)


def main():
    word = input("Please type in a string: ")
    print_substrings(word)

main()