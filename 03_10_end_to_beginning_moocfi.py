# Write your solution here

def print_reverse_order(word):
    index = 1
    while len(word) >= index:
        print(word[-1 * index])
        index += 1



def main():
    word = input("Please type in a string: ")
    print_reverse_order(word)

main()