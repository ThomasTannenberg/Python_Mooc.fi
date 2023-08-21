# Write your solution here
def remove_smallest(numbers: list):
    # This helps me to find the lowest numer in the given list
    find_lowest_list = [num for num in numbers]
    find_lowest_list.sort()
    lowest_number = find_lowest_list[0]

    # more easy solution to find the lowest:
    # lowest_number = min(numbers)


    print('DEBUG: the lowest number is: ', lowest_number)

    numbers.remove(lowest_number)



if __name__ == "__main__":
    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    print(numbers)