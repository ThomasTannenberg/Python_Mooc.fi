def longest_series_of_neighbours(list_of_numbers):
  
  current_length = 1
  longest_length = 1
  
  for i in range(1, len(list_of_numbers)):
    if list_of_numbers[i] == list_of_numbers[i - 1] or list_of_numbers[i] - list_of_numbers[i - 1] == 1:
      current_length += 1
    else:
      current_length = 1
    longest_length = max(longest_length, current_length)
  return longest_length


if __name__ == "__main__":
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))