def print_alternating_numbers():
    number = int(input("Please type in a number: "))

    if number < 1:
        print("Please enter a positive number.")
        return

    numbers = list(range(1, number + 1))
    i = 0
    j = len(numbers) - 1

    while i <= j:
        print(numbers[i])
        if i != j:
            print(numbers[j])
        i += 1
        j -= 1

print_alternating_numbers()

