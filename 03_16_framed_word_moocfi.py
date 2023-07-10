def framed_word(word):
    spaces = " " * ((28 - len(word)) // 2)
    extra_spaces = ""
    if len(word) %2 != 0:
        extra_spaces = " "
        print("*" * 30)
        print("*" + spaces + word + extra_spaces + spaces + "*")
        print("*" * 30)


    else:
        print("*" * 30)
        print("*" + spaces + word + spaces + "*")
        print("*" * 30)


def main():
    word = input("Word: ")
    framed_word(word)


main()
