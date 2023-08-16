# Write your solution here
def even_numbers(list):
    sorted_list = []
    for num in list:
      if num % 2 == 0:
         sorted_list.append(num)

    return sorted_list


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    new_list = even_numbers(my_list)
    print("original", my_list)
    print("new", new_list)