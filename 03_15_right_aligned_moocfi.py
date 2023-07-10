# Write your solution here
def print_right_aligned(word):
    filler = ("*" * (20 - len(word)))
    print(filler+word)

def main():
    word = input("Please type in a string: ")
    print_right_aligned(word)

main()