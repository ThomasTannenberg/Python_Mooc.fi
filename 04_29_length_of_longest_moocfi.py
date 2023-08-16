# Write your solution here
def length_of_longest(list):
  longest_string = ""
  for string in list:
    if len(string) > len(longest_string):
      longest_string = string

  return len(longest_string)



if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = length_of_longest(my_list)
    print(result)
