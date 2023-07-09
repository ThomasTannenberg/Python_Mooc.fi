# Write your solution here
def output(word, amount):
    print(word * amount)


def main():
    word = input("Please type in a string: ")
    amount = int(input("Please type in an amount: "))
    output(word, amount)

main()