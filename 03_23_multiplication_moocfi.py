# Write your solution here
def multiplication(number):

    for i in range(1, number + 1):
        for j in range(1, number + 1):
            result = i * j
            print(i, "x", j, "=", result)



def main():
    number = int(input("Please type in a number: "))
    multiplication(number)

main()