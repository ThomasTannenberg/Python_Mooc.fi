def calculate_sum(limit):
    current_sum = 0
    next_number = 1
    consecutive_numbers = [1]

    while current_sum < limit:
        current_sum += next_number
        next_number += 1
        consecutive_numbers.append(next_number)

    return current_sum, consecutive_numbers

def main():
    limit = int(input("Limit: "))
    result_sum, consecutive_numbers = calculate_sum(limit)
    consecutive_numbers_str = " + ".join(str(num) for num in consecutive_numbers)
    consecutive_numbers_str = consecutive_numbers_str[:-3]
    print("The consecutive sum:", consecutive_numbers_str, "=", result_sum)

main()
