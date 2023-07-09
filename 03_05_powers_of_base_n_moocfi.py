
def powers_of_two(limit, base):
    number = 1

    while number <= limit:
        print(number)
        number *= base

        

def main():
    limit = int(input("upper limit: "))
    base = int(input("Base: "))
    powers_of_two(limit, base)

main()