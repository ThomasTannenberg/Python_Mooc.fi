
def powers_of_two(limit):
    number = 1

    while number <= limit:
        print(number)
        number *= 2

        

def main():
    limit = int(input("upper limit: "))
    powers_of_two(limit)

main()