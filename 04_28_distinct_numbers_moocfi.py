# Write your solution here
def distinct_numbers(list):
  new_list = []
  seen = set()
  for num in list:
    if num not in seen:
      new_list.append(num)
      seen.add(num)
  new_list.sort()
  return new_list

if __name__ == "__main__":
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list)) # [1, 2, 3]