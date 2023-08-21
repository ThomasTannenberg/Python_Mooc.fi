# Write your solution here
def double_items(numbers: list):
    doubled_list = [num * 2 for num in numbers]
    return doubled_list

    #for num in numbers:
    #    doubled_list.append(num*2)
    #return doubled_list

    

if __name__ == "__main__":
    numbers = [0, 4, 5, 3, 11, -4]
    numbers_doubled = double_items(numbers)
    print('original:', numbers)
    print('doubled:', numbers_doubled)