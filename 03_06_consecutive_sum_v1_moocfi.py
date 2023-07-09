def calculate_sum(limit):
    current_sum = 0
    next_number = 1

    while current_sum < limit:
        current_sum += next_number
        next_number += 1

    return current_sum

def main():
    limit = int(input("Limit: "))
    result = calculate_sum(limit)
    print(result)

main()

